import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Generate sample live data
def generate_live_data(num_records):
    now = datetime.now()
    data = {
        'timestamp': [now - timedelta(seconds=i) for i in range(num_records)],
        'player_id': np.random.randint(1, 100000, num_records),
        'session_id': np.random.randint(1, 1000000, num_records),
        'game_id': np.random.choice(['game1', 'game2', 'game3'], num_records),
        'level': np.random.randint(1, 100, num_records),
        'score': np.random.randint(0, 10000, num_records),
        'items_collected': np.random.randint(0, 50, num_records),
        'time_played': np.random.randint(1, 3600, num_records),
        'in_app_purchases': np.random.choice([0, 1], num_records, p=[0.9, 0.1]),
        'device_type': np.random.choice(['mobile', 'tablet', 'pc'], num_records),
        'location': np.random.choice(['US', 'EU', 'Asia', 'Other'], num_records)
    }
    return pd.DataFrame(data)

# Generate and save live data
live_data = generate_live_data(1000000)  # 1 million records
live_data.to_csv('data/live_data.csv', index=False)
print("Live data generated and saved.")