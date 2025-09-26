from schemas import InputSchema, OutputSchema
from fastapi import FastAPI
from predict import get_prediction, make_batch_predictions
from typing import List

app = FastAPI()


@app.get("/")
def index():
    return {"message": "Welcome to out first ML predition API"}


@app.post("/predict", response_model=OutputSchema)
def predict(input_data: InputSchema):
    to_dict = input_data.model_dump()
    prediction = get_prediction(to_dict)
    return OutputSchema(median_house_value=round(prediction, 2))


@app.post("/batch-predictions", response_model=List[OutputSchema])
def batch_predict(data: List[InputSchema]):
    predictions = make_batch_predictions([d.model_dump() for d in data])
    return [
        OutputSchema(median_house_value=round(prediction, 2))
        for prediction in predictions
    ]
