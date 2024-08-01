# API Documentation

## Base URL
`https://api.gameanalytics.com/v1`

## Endpoints

### 1. Predict Player Churn

Predicts the likelihood of a player churning based on their gameplay data.

- **URL:** `/predict_churn`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "total_playtime": 1000,
    "total_score": 5000,
    "achievements_unlocked": 20,
    "max_level_reached": 50,
    "total_in_app_purchases": 100,
    "player_retention_days": 30,
    "average_session_duration": 3600
  }

  Response:
  ```json
  {
  "churn_prediction": 0,
  "churn_probability": 0.15
  }

### 2. Get Game Performance
Retrieves performance metrics for a specific game.

**URL:** `/game_performance/<game_id>`
**Method:** `GET`

Response:
```json
{
  "game_id": "game1",
  "total_playtime": 1000000,
  "avg_score": 5000,
  "total_revenue": 50000
}
```

### 3. Get Player Stats
Retrieves statistics for a specific player.

**URL:** `/player_stats/<player_id>`
**Method:** `GET`

Response:
```json
{
  "player_id": "player123",
  "total_playtime": 10000,
  "total_score": 50000,
  "achievements_unlocked": 30,
  "total_in_app_purchases": 500
}

