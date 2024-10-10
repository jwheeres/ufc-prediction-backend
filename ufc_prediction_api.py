from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

class FightPredictionRequest(BaseModel):
    fighter_1: str
    fighter_2: str

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/predict")
def predict(request: FightPredictionRequest):
    # Extract fighter names from the request
    fighter_1 = request.fighter_1
    fighter_2 = request.fighter_2

    # Placeholder for prediction logic
    return {"prediction": f"Predicting a winner between {fighter_1} and {fighter_2}"}

