from flask import Flask, request, render_template

import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Get form data
    tasapm = int(request.form["tasapm"])

    
    # Prepare features for prediction
    features = [
        tasapm
    ]
    
    features = np.array(features).reshape(1, -1)
    
    # Make prediction
    prediction = model.predict(features)
    
    # Return prediction result
    return render_template("result.html", prediction="{:.2f}%".format(float(prediction[0])))

if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=8000)