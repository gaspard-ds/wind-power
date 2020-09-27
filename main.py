"""Main Module"""
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score, train_test_split

import wind_constants as cst


def train_one_model(
    data: pd.DataFrame,
    features: List[str],
    target: str,
    estimator: Optional[Any] = None,
    split_quantile: float = 0.75,
    **kwargs: Any,
) -> Tuple[any, Dict[str, float]]:
    """[summary]

    :param data: Input data
    :type data: pd.DataFrame
    :param features: features for the model
    :type features: List[str]
    :param target: target of the model
    :type target: str
    :param estimator: sklearn estimator, defaults to None
    :type estimator: Optional[Any], optional
    :param split_quantile: ratio of the data used for training, defaults to 0.75
    :type split_quantile: float, optional
    :return: model and scores
    :rtype: Tuple[any, Dict[str, float]]
    """
    estimator = estimator if estimator is not None else LinearRegression
    data = data[features + [target]].dropna()
    X_train, X_test, y_train, y_test = train_test_split(
        data[features], data[target], train_size=split_quantile, shuffle=False
    )
    model = estimator(**kwargs)
    model.fit(X=X_train, y=y_train)

    scores = {
        "r2_train": round(model.score(X=X_train, y=y_train), 3),
        "r2_test": round(model.score(X=X_test, y=y_test), 3),
        "r2_CV_test": list(
            cross_val_score(
                estimator=model, X=X_test, y=y_test, scoring="r2", cv=5, n_jobs=4
            ).round(2)
        ),
    }
    return model, scores


def get_absolute_predictions(data: pd.DataFrame, model: Any) -> pd.Series(dtype="float64"):
    predictions = pd.Series(data=model.predict(X=data), index=data.index)
    absolute_prediction = predictions * data["capacity"]
    absolute_prediction.name = "absolute_predictions_MWh"
    return absolute_prediction


PROCESSED_DATA = "data/processed/processed_uncleaned.joblib"

if __name__ == "__main__":
    data = joblib.load(Path(__file__).parent.resolve() / PROCESSED_DATA)
    model, scores = train_one_model(data=data, features=cst.FEATURES, target=cst.TARGET)
    joblib.dump(model, Path(__file__).parent.resolve() / "models/lr_quantile_75")

    print(scores)
