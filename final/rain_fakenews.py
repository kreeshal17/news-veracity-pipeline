import re
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib

# # Preprocessing function (for FunctionTransformer)
# def preprocessing(texts):
#     cleaned_texts = []
#     for text in texts:
#         text = text.lower()
#         text = re.sub(r"[^a-z\s]", "", text)
#         cleaned_texts.append(text)  # Fixed: append to list
#     return cleaned_texts  # Fixed: return the list

# # Wrap function into FunctionTransformer
# transform = FunctionTransformer(preprocessing, validate=False)

data = pd.read_csv("news.csv")
df = pd.DataFrame(data)
df = df.drop(columns=["Unnamed: 0"])
df["content"] = df["title"] + " " + df["text"]

X = df["content"]  # Fixed: removed .apply(preprocessing)
y = df["label"]

# Train/test split
x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Build pipeline
model = Pipeline([
    # ("preprocessing", transform),
    ("vectorizer", TfidfVectorizer(stop_words="english")),
    ("clf", LogisticRegression(max_iter=200))
])

# Train
model.fit(x_train, y_train)

joblib.dump(model, "fnews.pkl")
loaded = joblib.load("fnews.pkl")

# Fixed: define text before using it
sample_text = ["This is a sample news article"]
prediction = loaded.predict(sample_text)
print("Prediction:", prediction)

# Evaluate
print("Train Accuracy:", model.score(x_train, y_train))
print("Test Accuracy:", model.score(x_test, y_test))