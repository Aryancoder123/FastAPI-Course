from pydantic import BaseModel, Field, StrictInt


class InputSchema(BaseModel):
    longitude: float
    latitude: float
    housing_median_age: StrictInt
    total_rooms: StrictInt = Field(..., gt=0)
    total_bedrooms: StrictInt = Field(..., gt=0)
    population: int = Field(..., gt=0)
    households: int = Field(..., gt=0)
    median_income: float = Field(..., gt=0)


class OutputSchema(BaseModel):
    median_house_value: float
