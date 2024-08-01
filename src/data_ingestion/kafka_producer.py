from kafka import KafkaProducer
import json
import pandas as pd
import time

def kafka_producer():
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                             value_serializer=lambda x: json.dumps(x).encode('utf-8'))

    df = pd.read_csv('data/live_data.csv')
    
    for _, row in df.iterrows():
        data = row.to_dict()
        producer.send('game_events', value=data)
        time.sleep(0.1)  # Simulate real-time data

    producer.close()

if __name__ == "__main__":
    kafka_producer()