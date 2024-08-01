import pytest
from kafka import KafkaProducer
from src.data_ingestion.kafka_producer import kafka_producer

def test_kafka_producer():
    producer = kafka_producer()
    assert isinstance(producer, KafkaProducer)

def test_message_sent():
    producer = kafka_producer()
    future = producer.send('test_topic', b'test_message')
    result = future.get(timeout=10)
    assert result.topic == 'test_topic'
    assert result.partition == 0