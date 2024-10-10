from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/predict")
def predict(fighter_1: str, fighter_2: str):
    # Placeholder for prediction logic
    return {"prediction": f"Predicting a winner between {fighter_1} and {fighter_2}"}
