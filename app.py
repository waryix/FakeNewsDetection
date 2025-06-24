"""
from flask import Flask, request, jsonify
from flask_cors import CORS 
import pickle

app = Flask(__name__)
CORS(app)

# Load the trained model
with open('fake_news_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
def home():
    return "Fake News Detection API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json  # Get JSON data
    text = data['text']
    
    prediction = model.predict([text])[0]  # Predict
    result = "FAKE" if prediction == 1 else "REAL"
    
    return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
"""


from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")  # This serves the frontend

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    text = data.get("text", "")

    # Dummy prediction logic (replace with ML model)
    prediction = "FAKE" if "fake" in text.lower() else "REAL"

    return jsonify({"prediction": prediction})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)  # Allow access on local network

