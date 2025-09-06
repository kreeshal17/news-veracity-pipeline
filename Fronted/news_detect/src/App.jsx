import React, { useState } from "react";
import axios from "axios";

function App() {
  const [text, settext] = useState("");
  const [prediction, setprediction] = useState("");

  const handlesubmit = async () => {
    if (!text.trim()) {
      alert("enter the text");
      return;
    }
    const response = await axios.post("http://127.0.0.1:5000/predict", {
      text: text,
    });
    setprediction(response.data.prediction);
    settext("");
  };

  return (
    <>
      <div className="w-full min-h-screen bg-gradient-to-br from-purple-600 via-pink-500 to-indigo-700 flex items-center justify-center p-6">
        <div className="bg-white/90 backdrop-blur-xl shadow-2xl rounded-2xl w-full max-w-2xl p-8 flex flex-col items-center">
          {/* Title */}
          <h1 className="text-3xl font-extrabold text-gray-800 mb-6 tracking-wide">
            📰 Fake News Detector
          </h1>

          {/* Text Area */}
          <textarea
            className="w-full h-40 p-4 border-2 border-gray-200 rounded-xl mb-6 focus:outline-none focus:ring-4 focus:ring-indigo-400 resize-none text-gray-800 placeholder-gray-400 transition"
            rows="5"
            placeholder="Paste news text here..."
            value={text}
            onChange={(e) => settext(e.target.value)}
          />

          {/* Submit Button */}
          <button
            onClick={handlesubmit}
            className="w-full bg-gradient-to-r from-indigo-500 to-purple-600 text-white font-semibold px-6 py-3 rounded-xl shadow-lg hover:scale-105 transition-transform duration-300"
          >
            🚀 Analyze
          </button>

          {/* Prediction Result */}
          {prediction && (
            <div className="mt-8 w-full text-center">
              <p className="text-lg font-medium text-gray-700">
                The news is:
              </p>
              <p
                className={`mt-2 text-2xl font-bold ${
                  prediction.toLowerCase() === "fake"
                    ? "text-red-600"
                    : "text-green-600"
                }`}
              >
                {prediction}
              </p>
            </div>
          )}
        </div>
      </div>
    </>
  );
}

export default App;
