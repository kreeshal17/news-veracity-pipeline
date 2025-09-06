from flask import Flask, jsonify, request
import joblib
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
# Load trained pipeline
loaded = joblib.load("fnews.pkl")

@app.route("/")
def home():
    return "The app is running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data["text"]
    
    # Pipeline handles preprocessing + vectorizing
    prediction = loaded.predict([text])

    return jsonify({"prediction": prediction[0]})

if __name__ == "__main__":
    app.run(debug=True)
