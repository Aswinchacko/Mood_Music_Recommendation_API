import pandas as pd
import requests
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.utils.class_weight import compute_class_weight

# Load dataset from file
def load_dataset(path):
    df = pd.read_csv(path, sep=";", header=None, names=["text", "label"])
    return df

# Train logistic regression text classifier
def train_model():
    df = load_dataset("dataset/train_cleaned.txt")
    classes = df["label"].unique()
    weights = compute_class_weight(class_weight="balanced", classes=classes, y=df["label"])
    class_weights = dict(zip(classes, weights))

    model = Pipeline([
        ("tfidf", TfidfVectorizer()),
        ("clf", LogisticRegression(max_iter=300, class_weight=class_weights))
    ])
    model.fit(df["text"], df["label"])
    return model

# Fetch songs using Last.fm API
def get_music_from_lastfm(mood):
    import time

    mood_keywords = {
        "joy": ["happy", "uplifting"],
        "sadness": ["sad", "emotional"],
        "anger": ["angry", "rock"],
        "love": ["romantic", "love"],
        "fear": ["dark", "ambient"],
        "surprise": ["party", "electronic"]
    }

    queries = mood_keywords.get(mood, [mood])
    api_key = "49a9d0d00254c89a2d88f379851114fc"
    songs = []

    for tag in queries:
        url = f"http://ws.audioscrobbler.com/2.0/?method=tag.gettoptracks&tag={tag}&api_key={api_key}&format=json"
        try:
            res = requests.get(url)
            res.raise_for_status()
            data = res.json()
        except Exception as e:
            return [f"Last.fm API error: {e}"]

        for track in data.get("tracks", {}).get("track", [])[:5]:
            title = track.get("name", "")
            artist = track.get("artist", {}).get("name", "")
            link = track.get("url", "")
            if title and artist:
                songs.append(f"{title} – {artist} ({link})")

        if songs:
            break
        time.sleep(0.2)

    return songs if songs else ["No tracks found from Last.fm."]

# Exposed to FastAPI
def recommend_songs(mood):
    return get_music_from_lastfm(mood)
