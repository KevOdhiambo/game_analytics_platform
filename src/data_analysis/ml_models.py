import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def train_churn_prediction_model():
    df = pd.read_csv('data/historical_data.csv')
    
    features = ['total_playtime', 'total_score', 'achievements_unlocked', 'max_level_reached', 
                'total_in_app_purchases', 'player_retention_days', 'average_session_duration']
    
    X = df[features]
    y = df['player_churn']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"Churn Prediction Model Accuracy: {accuracy:.2f}")
    
    return model

if __name__ == "__main__":
    churn_model = train_churn_prediction_model()