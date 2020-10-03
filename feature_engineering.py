import pandas as pd
import sklearn.preprocessing as pp


def polynomial_features_labeled(input_df: pd.DataFrame, power: int = 2) -> pd.DataFrame:
    """Wrapper for the sklearn preprocessing function. Adapted from StackOverflow"""

    poly = pp.PolynomialFeatures(degree=power)
    output_nparray = poly.fit_transform(X=input_df)
    powers_nparray = poly.powers_

    input_feature_names = list(input_df.columns)
    target_feature_names = ["Constant Term"]
    for feature_distillation in powers_nparray[1:]:
        intermediary_label = ""
        final_label = ""
        for i in range(len(input_feature_names)):  # pylint:disable=consider-using-enumerate
            if feature_distillation[i] == 0:
                continue
            else:
                variable = input_feature_names[i]
                power = feature_distillation[i]
                if power == 1:
                    intermediary_label = "%s" % (variable)
                else:
                    intermediary_label = "%s^%d" % (variable, power)
                if final_label == "":  # If the final label isn't yet specified
                    final_label = intermediary_label
                else:
                    final_label = final_label + " x " + intermediary_label
        target_feature_names.append(final_label)
    output_df = pd.DataFrame(output_nparray, columns=target_feature_names, index=input_df.index)
    return output_df


def add_inertia(dataframe: pd.DataFrame, steps=2) -> pd.DataFrame:
    data = dataframe.copy()
    for column in data:
        for step in range(1, steps + 1):
            data[f"{column}_diff_{step}"] = data[column].diff(step)
            data[f"{column}_shift_{step}"] = data[column].shift(step)
    return data


def feature_engineering(dataframe: pd.DataFrame, power=2, steps=2) -> pd.DataFrame:
    data = dataframe.copy()
    data_inertia = add_inertia(dataframe=data, steps=steps)
    data_poly = polynomial_features_labeled(input_df=data, power=power)

    data = pd.concat(objs=[data_inertia, data_poly], axis="columns")
    data = data.loc[:, ~data.columns.duplicated()]
    return data.dropna()
