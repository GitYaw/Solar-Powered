from flask import Flask, render_template, request
import numpy as np
from tensorflow.keras.models import load_model

app = Flask(__name__)

# Load your pre-trained machine learning model
model = load_model('tiny_200.h5')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        try:
            # Get user input from the form
            time = float(request.form.get("time"))
            cloudcover = float(request.form.get("cloudcover"))
            dew = float(request.form.get("dew"))
            humidity = float(request.form.get("humidity"))
            precip = float(request.form.get("precip"))
            precipprob = float(request.form.get("precipprob"))
            solarenergy = float(request.form.get("solarenergy"))
            solarradiation = float(request.form.get("solarradiation"))
            sunelevation = float(request.form.get("sunelevation"))
            temp = float(request.form.get("temp"))
            uvindex = float(request.form.get("uvindex"))

            # Create an array with the input data
            input_data = np.array([[time, cloudcover, dew, humidity, precip, precipprob,
                                    solarenergy, solarradiation, sunelevation, temp, uvindex]])

            # Make prediction using your model
            prediction = model.predict(input_data)

            # Format the prediction for display
            predicted_whProduced = prediction[0][0]

            return render_template("result.html", prediction=predicted_whProduced)
        except Exception as e:
            return f"An error occurred: {e}"

    else:
        return "Something went wrong. Please try again."

if __name__ == "__main__":
    app.run(debug=True)