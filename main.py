# import your_ml_model  # Replace with your machine learning model import
from flask import Flask, render_template, request
import numpy as np
from tensorflow.keras.models import load_model

app = Flask(__name__)

# Load your pre-trained machine learning model here
model = load_model('tiny_200.h5')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        # Get user input from the form
        input_data = request.form.get("input")

        # Preprocess the input data for your model (if needed)
        # ... your data preprocessing code here ...

        # Make prediction using your model
        prediction = input_data # model.predict([preprocessed_data])  # Assuming a list input

        # Format the prediction for display
        predicted_class = prediction # prediction[0]  # Assuming single class output

        return render_template("result.html", prediction=predicted_class)

    else:
        return "Something went wrong. Please try again."

if __name__ == "__main__":
    app.run(debug=True)

# if __name__ == '__main__':
#   app.run(host='0.0.0.0', port=5000)
