import numpy as np
import joblib
from typing import List

model = joblib.load("model.joblib")


def get_prediction(data: dict) -> float:
    input_feature = np.array(
        [
            [
                data["longitude"],
                data["latitude"],
                data["housing_median_age"],
                data["total_rooms"],
                data["total_bedrooms"],
                data["population"],
                data["households"],
                data["median_income"],
            ]
        ]
    )
    return model.predict(input_feature)[0]


def make_batch_predictions(new_data: List[dict]) -> np.array:
    input_data = np.array(
        [
            [
                data["longitude"],
                data["latitude"],
                data["housing_median_age"],
                data["total_rooms"],
                data["total_bedrooms"],
                data["population"],
                data["households"],
                data["median_income"],
            ]
            for data in new_data
        ]
    )
    return model.predict(input_data)
