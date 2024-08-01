CREATE TABLE game_analytics.raw_game_data (
    event_timestamp TIMESTAMP,
    player_id STRING,
    session_id STRING,
    game_id STRING,
    level INT64,
    score INT64,
    items_collected INT64,
    time_played INT64,
    in_app_purchases FLOAT64,
    device_type STRING,
    location STRING
);

CREATE TABLE game_analytics.game_performance_summary (
    game_id STRING,
    total_playtime INT64,
    avg_score FLOAT64,
    total_revenue FLOAT64
);