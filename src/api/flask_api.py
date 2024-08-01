from flask import Flask, request, jsonify
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load('churn_prediction_model.joblib')

@app.route('/predict_churn', methods=['POST'])
def predict_churn():
    data = request.json
    df = pd.DataFrame(data, index=[0])
    
    prediction = model.predict(df)
    probability = model.predict_proba(df)[0][1]
    
    return jsonify({
        'churn_prediction': int(prediction[0]),
        'churn_probability': float(probability)
    })

if __name__ == '__main__':
    app.run(debug=True)