from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return "Student Performance Predictor API is live"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Example: you must encode values if needed here before prediction
    input_data = [
        data['gender'],
        data['race_ethnicity'],
        data['parental_level_of_education'],
        data['lunch'],
        data['test_preparation_course']
    ]

    prediction = model.predict([input_data])
    result = 'Pass' if prediction[0] == 1 else 'Fail'
    return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run(debug=True)
