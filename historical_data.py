import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Generate sample historical data
def generate_historical_data(num_records):
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)
    
    data = {
        'date': pd.date_range(start=start_date, end=end_date, periods=num_records),
        'player_id': np.random.randint(1, 1000000, num_records),
        'game_id': np.random.choice(['game1', 'game2', 'game3'], num_records),
        'total_playtime': np.random.randint(0, 100000, num_records),
        'total_score': np.random.randint(0, 1000000, num_records),
        'achievements_unlocked': np.random.randint(0, 100, num_records),
        'max_level_reached': np.random.randint(1, 100, num_records),
        'total_in_app_purchases': np.random.randint(0, 1000, num_records),
        'player_retention_days': np.random.randint(1, 365, num_records),
        'average_session_duration': np.random.randint(1, 7200, num_records),
        'player_churn': np.random.choice([0, 1], num_records, p=[0.7, 0.3])
    }
    return pd.DataFrame(data)

# Generate and save historical data
historical_data = generate_historical_data(5000000)  # 5 million records
historical_data.to_csv('data/historical_data.csv', index=False)
print("Historical data generated and saved.")