# 🎧 Mood Music Recommender

A machine learning-powered web API that analyzes text input to predict emotional mood and recommends personalized music tracks using the Last.fm API.

## 🚀 Features

- **Text-based Mood Analysis**: Analyzes user text input to predict emotional states
- **Intelligent Music Recommendations**: Suggests songs based on predicted mood using Last.fm API
- **FastAPI REST API**: Modern, fast, and auto-documented API endpoints
- **Machine Learning Pipeline**: TF-IDF vectorization with Logistic Regression classifier
- **Multi-label Classification**: Supports 6 emotional categories: joy, sadness, anger, love, fear, surprise

## 🏗️ Architecture

```
Music Web App/
├── api.py                 # FastAPI application entry point
├── model/
│   ├── mood_model.py      # ML model training and prediction logic
│   ├── clean_dataset.py   # Dataset preprocessing utilities
│   └── requirements.txt   # Python dependencies
└── dataset/
    ├── train_cleaned.txt  # Training dataset (cleaned)
    ├── test_cleaned.txt   # Test dataset (cleaned)
    └── val_cleaned.txt    # Validation dataset (cleaned)
```

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd "Music Web App"
   ```

2. **Install dependencies**
   ```bash
   pip install -r model/requirements.txt
   ```

3. **Run the application**
   ```bash
   uvicorn api:app --reload
   ```

The API will be available at `http://localhost:8000`

## 📖 API Documentation

### Endpoints

#### `GET /`
Welcome endpoint that returns a greeting message.

**Response:**
```json
{
  "message": "Welcome to the Mood Music Recommender API!"
}
```

#### `POST /predict`
Analyzes text input and returns mood prediction with music recommendations.

**Request Body:**
```json
{
  "text": "I'm feeling really happy today!"
}
```

**Response:**
```json
{
  "mood": "joy",
  "songs": [
    "Happy – Pharrell Williams (https://www.last.fm/music/Pharrell+Williams/_/Happy)",
    "Walking on Sunshine – Katrina & The Waves (https://www.last.fm/music/Katrina+%26+The+Waves/_/Walking+on+Sunshine)"
  ]
}
```

### Interactive API Documentation

Once the server is running, visit:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## 🧠 Machine Learning Model

### Model Architecture
- **Text Vectorization**: TF-IDF (Term Frequency-Inverse Document Frequency)
- **Classifier**: Logistic Regression with balanced class weights
- **Training Data**: Preprocessed text dataset with mood labels
- **Supported Moods**: joy, sadness, anger, love, fear, surprise

### Model Training Process
1. **Data Loading**: Reads from `dataset/train_cleaned.txt`
2. **Text Preprocessing**: Lowercase, special character removal, whitespace normalization
3. **Feature Extraction**: TF-IDF vectorization of text input
4. **Classification**: Logistic Regression with balanced class weights for handling imbalanced data

## 🎵 Music Recommendations

The system uses the Last.fm API to fetch music recommendations based on predicted mood:

- **joy** → happy, uplifting tracks
- **sadness** → sad, emotional tracks  
- **anger** → angry, rock tracks
- **love** → romantic, love tracks
- **fear** → dark, ambient tracks
- **surprise** → party, electronic tracks

## 📊 Dataset

The model is trained on a cleaned text dataset with the following structure:
- **Format**: `text;mood_label`
- **Training Set**: `dataset/train_cleaned.txt` (1.6MB)
- **Test Set**: `dataset/test_cleaned.txt` (204KB)
- **Validation Set**: `dataset/val_cleaned.txt` (201KB)

### Data Preprocessing
The `clean_dataset.py` script performs:
- Text normalization (lowercase)
- Special character removal
- Whitespace normalization
- Label standardization

## 🔧 Development

### Project Structure
```
├── api.py                 # FastAPI application
├── model/
│   ├── mood_model.py      # ML model logic
│   ├── clean_dataset.py   # Data preprocessing
│   └── requirements.txt   # Dependencies
└── dataset/              # Training datasets
```

### Key Dependencies
- **FastAPI**: Modern web framework for APIs
- **scikit-learn**: Machine learning library
- **pandas**: Data manipulation
- **requests**: HTTP library for API calls
- **uvicorn**: ASGI server

### Running in Development
```bash
# Start with auto-reload
uvicorn api:app --reload --host 0.0.0.0 --port 8000

# Start in production mode
uvicorn api:app --host 0.0.0.0 --port 8000
```

## 🚀 Deployment

### Docker (Recommended)
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY . .

RUN pip install -r model/requirements.txt

EXPOSE 8000
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Environment Variables
- `LASTFM_API_KEY`: Your Last.fm API key (optional, uses default key)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 🙏 Acknowledgments

- **Last.fm API**: For music recommendations
- **scikit-learn**: For machine learning capabilities
- **FastAPI**: For the modern web framework

---

**Made with ❤️ for music lovers everywhere** 