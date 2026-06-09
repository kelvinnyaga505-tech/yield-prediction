from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Home route
@app.route('/')
def home():
    return "AI Crop Yield Prediction Backend Running..."

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():

    data = request.get_json()
    print(data)
    rainfall = float(data['rainfall'])
    humidity = float(data['humidity'])
    temperature = float(data['temperature'])
    soilph = float(data['soilph'])
    crop_type = data['cropType']

    # Prediction formula
    prediction = (
        (rainfall * 0.05) +
        (humidity * 0.03) +
        (soilph * 2) -
        (temperature * 0.4)
    )

    prediction = round(prediction, 2)

    # Crop recommendation logic
    if prediction >= 80:
        status = "Excellent Yield Expected"

    elif prediction >= 50:
        status = "Good Yield Expected"

    elif prediction >= 30:
        status = "Average Yield Expected"

    else:
        status = "Low Yield Expected"

    return jsonify({
        "crop": crop_type,
        "predicted_yield": prediction,
        "status": status
    })

# Run server
if __name__ == '__main__':
    app.run(debug=True)