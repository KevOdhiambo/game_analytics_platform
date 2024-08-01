import pytest
from flask import json
from src.api.flask_api import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_predict_churn(client):
    data = {
        'total_playtime': 1000,
        'total_score': 5000,
        'achievements_unlocked': 20,
        'max_level_reached': 50,
        'total_in_app_purchases': 100,
        'player_retention_days': 30,
        'average_session_duration': 3600
    }
    response = client.post('/predict_churn', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 200
    assert 'churn_prediction' in json.loads(response.data)
    assert 'churn_probability' in json.loads(response.data)