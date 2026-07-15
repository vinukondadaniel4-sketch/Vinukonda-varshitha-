from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load("model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    temperature = float(request.form["temperature"])
    humidity = float(request.form["humidity"])
    occupancy = float(request.form["occupancy"])
    hour = float(request.form["hour"])

    data = pd.DataFrame([[temperature, humidity, occupancy, hour]],
                        columns=["Temperature", "Humidity", "Occupancy", "Hour"])

    prediction = model.predict(data)[0]

    return render_template("index.html", prediction=round(prediction, 2))

if __name__ == "__main__":
    app.run(debug=True)