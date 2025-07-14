
from fastapi import FastAPI
from pydantic import BaseModel
from model.mood_model import train_model, recommend_songs

app = FastAPI(title="🎧 Mood Music Recommender")

model = train_model()

class MoodRequest(BaseModel):
    text: str

class MoodResponse(BaseModel):
    mood: str
    songs: list[str]

@app.get("/")
def home():
    return {"message": "Welcome to the Mood Music Recommender API!"}

@app.post("/predict", response_model=MoodResponse)
def predict_mood(req: MoodRequest):
    mood = model.predict([req.text])[0]
    songs = recommend_songs(mood)
    return {"mood": mood, "songs": songs}
