from pathlib import Path

import joblib
import pandas as pd
import wind_constants as cst

RAW_CAPACITY = "data/raw/parc-regional-annuel-prod-eolien-solaire.csv"
RAW_PRODUCTION = "data/raw/eco2mix-regional-cons-def.csv"
RAW_WEATHER = "data/raw/donnees-synop-essentielles-omm.csv"

SELECTION_CAPACITY = "data/selection/parc-eolien.joblib"
SELECTION_PRODUCTION = "data/selection/production.joblib"
SELECTION_WEATHER = "data/selection/weather.joblib"

PROCESSED_DATA = "data/processed/processed_uncleaned.joblib"


def data_selection_capacity() -> None:
    data_path = Path(__file__).parent.resolve() / RAW_CAPACITY
    data = pd.read_csv(data_path, sep=";")
    data = data.drop(
        columns=["Parc installé solaire (MW)", "Géo-shape région", "Géo-point région"]
    )
    joblib.dump(value=data, filename=SELECTION_CAPACITY)


def data_selection_production() -> None:
    data_path = Path(__file__).parent.resolve() / RAW_PRODUCTION
    data = pd.read_csv(data_path, sep=";")
    data = data[cst.TO_KEEP_PRODUCTION]
    joblib.dump(value=data, filename=SELECTION_PRODUCTION)


def data_selection_weather() -> None:
    data_path = Path(__file__).parent.resolve() / RAW_WEATHER
    data = pd.read_csv(data_path, sep=";")
    data = data[cst.TO_KEEP_WEATHER]
    joblib.dump(value=data, filename=SELECTION_WEATHER)


def data_merge() -> None:
    capacity = joblib.load(Path(__file__).parent.resolve() / SELECTION_CAPACITY)
    weather = joblib.load(Path(__file__).parent.resolve() / SELECTION_WEATHER)
    production = joblib.load(Path(__file__).parent.resolve() / SELECTION_PRODUCTION)

    # Linear Interpolation for capacity
    # Index for the data is set at 3H to match weather granularity
    date_range_capacity = pd.date_range(
        start="2001-01-01 01:00:00",
        end="2020-07-31 23:00:00",
        freq="180T",
        tz="Europe/Paris",
    )
    data = pd.DataFrame(index=date_range_capacity)
    yearly_capacity = capacity.groupby(by="Année").sum()

    # There is a trick here : index starts at 1 AM in order to align with production index later
    yearly_capacity.index = pd.date_range(
        start="2002-01-01 01:00:00",
        end="2020-01-01 01:00:00",
        freq="YS",
        tz="Europe/Paris",
    )
    data["capacity"] = yearly_capacity["Parc installé éolien (MW)"]
    data = data.interpolate("linear")

    # Adding production data to our global dataframe
    # Decided to model the entire country's production, but could have opted for a region instead
    data_production = production.groupby(by="Date - Heure").sum()
    data_production.index = pd.to_datetime(data_production.index, utc=True)
    data_production.index = pd.DatetimeIndex(data_production.index)

    # Again here the 3H granularity is to match weather data granularity
    data_production = data_production.resample("180T").sum().tz_convert("Europe/Paris")
    data["production"] = data_production["Eolien (MW)"]

    # Production is average the power (MW) over an half hour
    # Since we resampled, it's now power production (MWH) over 3 hours
    # In order to keep relative production bewteen 0 and 1, we need to divide by 6
    data["relative_production"] = data["production"] / (data["capacity"] * 6)

    # Integrating averaged weather data to global dataframe
    data = data.truncate(before="2013-01-01 00:00:00+1")
    data_weather = weather.groupby("Date").mean()
    data_weather.index = pd.to_datetime(data_weather.index)
    data["speed"] = data_weather["Vitesse du vent moyen 10 mn"]
    data["direction"] = data_weather["Direction du vent moyen 10 mn"]
    data["temperature"] = data_weather["Température"]
    data["pressure"] = data_weather["Pression station"]
    data["gust"] = data_weather["Rafales sur une période"]
    data = data.assign(month=lambda x: x.index.month)

    # Wind speed and direction for each region
    for code, _ in cst.CODE_REGIONS.items():
        weather_region = weather[weather["region (code)"] == code].groupby("Date").mean()
        weather_region.index = pd.to_datetime(weather_region.index)
        data[f"speed_{code}"] = weather_region["Vitesse du vent moyen 10 mn"]
        data[f"direction_{code}"] = weather_region["Direction du vent moyen 10 mn"]

    joblib.dump(data, Path(__file__).parent.resolve() / PROCESSED_DATA)


if __name__ == "__main__":
    data_selection_capacity()
    data_selection_production()
    data_selection_weather()
    data_merge()
