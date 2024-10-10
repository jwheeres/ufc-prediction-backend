from fastapi import FastAPI

# Create an instance of the FastAPI class
app = FastAPI()

# Define a simple route to verify everything works
@app.get("/")
def read_root():
    return {"Hello": "World"}

# Define a route for predictions
@app.post("/predict")
def predict(fighter_1: str, fighter_2: str):
    # Placeholder for prediction logic
    return {"prediction": f"Predicting a winner between {fighter_1} and {fighter_2}"}

