from pathlib import Path

import pandas as pd


def test_car_crashes_dataset_exists() -> None:
    data_path = Path("data") / "car_crashes.csv"
    assert data_path.exists(), "data/car_crashes.csv should exist"


def test_car_crashes_dataset_not_empty() -> None:
    df = pd.read_csv(Path("data") / "car_crashes.csv")
    assert not df.empty, "car_crashes dataset should not be empty"
