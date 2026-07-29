from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "ML service works"}

@app.get("/health")
def health():
    return {"status": "OK"}

@app.post("/predict")
def predict():
    return {"digit": 5, "confidence": 0.98}