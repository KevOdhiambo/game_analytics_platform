# Data Dictionary

## Raw Game Data

| Field Name | Data Type | Description |
|------------|-----------|-------------|
| event_timestamp | TIMESTAMP | Time when the event occurred |
| player_id | STRING | Unique identifier for the player |
| session_id | STRING | Unique identifier for the play session |
| game_id | STRING | Identifier for the game being played |
| level | INTEGER | Current level of the player |
| score | INTEGER | Player's score in the current session |
| items_collected | INTEGER | Number of items collected in the session |
| time_played | INTEGER | Duration of the play session in seconds |
| in_app_purchases | FLOAT | Amount spent on in-app purchases in the session |
| device_type | STRING | Type of device used (e.g., mobile, tablet, pc) |
| location | STRING | Player's geographic location |

## Player Sessions

| Field Name | Data Type | Description |
|------------|-----------|-------------|
| session_id | UUID | Unique identifier for the session |
| player_id | STRING | Unique identifier for the player |
| game_id | STRING | Identifier for the game being played |
| start_time | TIMESTAMP | Start time of the session |
| end_time | TIMESTAMP | End time of the session |
| duration | INTEGER | Duration of the session in seconds |
| score | INTEGER | Total score achieved in the session |

## Game Performance Summary

| Field Name | Data Type | Description |
|------------|-----------|-------------|
| game_id | STRING | Identifier for the game |
| total_playtime | INTEGER | Total playtime across all players in seconds |
| avg_score | FLOAT | Average score across all players |
| total_revenue | FLOAT | Total revenue generated from in-app purchases |