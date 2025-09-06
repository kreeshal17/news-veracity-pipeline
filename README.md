# News Veracity Pipeline

A machine learning project for **Fake News Detection** with a full-stack deployment.

- **Backend (Flask)** → Handles model inference using a trained ML pipeline
- **Frontend (React + Tailwind)** → User-friendly interface for text input and predictions
- **Achieved 93–95% accuracy** with NLP preprocessing (spaCy), TF-IDF vectorization, and Logistic Regression
- Model persisted using **joblib** for production use

---

## 📁 Project Structure

```
news-veracity-pipeline/
│
├── backend/
│   ├── app.py                # Flask API for prediction
│   ├── train_fakenews.py     # Model training + preprocessing
│   ├── fnews.pkl             # Trained pipeline (joblib dump)
│   ├── news.csv              # Dataset
│   └── requirements.txt      # Dependencies
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
├── project2.ipynb           # Jupyter notebook for exploration
├── README.md
└── .gitignore
```

---

## ✨ Features

- **End-to-end ML lifecycle**: preprocessing → feature extraction → training → evaluation → deployment
- Preprocessing with **spaCy** (lemmatization, stopword removal)
- Feature extraction with **TF-IDF Vectorizer**
- Classification using **Logistic Regression**
- Model serialization via **joblib**
- Achieved **93–95% accuracy** on dataset

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/kreeshal17/news-veracity-pipeline.git
cd news-veracity-pipeline
```

### 2. Backend (Flask API)

```bash
cd backend
pip install -r requirements.txt
python app.py
```

**Runs on:** `http://127.0.0.1:5000`

### 3. Frontend (React + Tailwind)

```bash
cd frontend
npm install
npm start
```

**Runs on:** `http://localhost:3000`

---

## 💻 Usage

1. Input a news headline or full text in the frontend
2. Backend Flask API loads the joblib pipeline
3. Returns prediction: **REAL** or **FAKE**

---

## 🤖 Model Details

**Pipeline steps:**
- Preprocessing (spaCy-based text cleaning + lemmatization)
- Feature extraction via TF-IDF
- Classification with Logistic Regression

**Dataset:** `news.csv`  
**Accuracy:** 93–95%

---

## 📋 Requirements (Backend)

Add these in `requirements.txt`:

```
Flask
pandas
scikit-learn
spacy
joblib
numpy
```

**Note:** Also run `python -m spacy download en_core_web_sm`

Frontend dependencies handled via `package.json`.

---

## 🛠️ Tech Stack

- **Machine Learning:** scikit-learn, spaCy, joblib, pandas
- **Backend:** Flask
- **Frontend:** React, Tailwind CSS
- **Deployment:** Localhost

---

## 🚀 Future Enhancements

- Deploy on cloud platforms (Heroku, Render, Vercel)
- Expand dataset for robustness
- Add REST endpoints for batch predictions

---

## 👨‍💻 Author

**Krishal Karna**  
GitHub: [@kreeshal17](https://github.com/kreeshal17)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
