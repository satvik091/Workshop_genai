from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

# Intialise FastAPI app
app= FastAPI(title="Sentiment Analysis Api")

#define request body schema
class TextInput(BaseModel):
    text: str

model=pipeline("sentiment-analysis")

@app.get("/")
def home():
    return {"message": "Welcome to My Application"}

@app.post("/predict")
def predict(input: TextInput):
    """Predicting sentiment"""
    result=model(input.text)[0]
    return {"label":result["label"],"score":result["score"]}

