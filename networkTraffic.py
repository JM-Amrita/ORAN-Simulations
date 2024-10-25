import numpy as np
import pymongo
from pymongo import MongoClient
from datetime import datetime, timedelta


def connect_to_mongo(uri="/", db_name="5GSpectrum", collection_name="spectrumData-Sim"):
    """Establish connection to MongoDB."""
    client = MongoClient(uri)
    db = client[db_name]
    collection = db[collection_name]
    return collection

def generate_traffic_data(frequencies, time_steps, traffic_level):
    """Generates traffic data based on the given frequencies and traffic level."""
    traffic_std = {
        'low': 0.1,
        'medium': 0.3,
        'high': 0.5
    }
    
    std_dev = traffic_std.get(traffic_level, 0.3)
    traffic_data = 0.5 + np.random.normal(0, std_dev, (time_steps, len(frequencies)))
    return np.clip(traffic_data, 0, 1)

def save_to_mongo(collection, data, frequencies, traffic_level, start_time):
    """Saves the generated traffic data to MongoDB."""
    for time_step, traffic in enumerate(data):
        timestamp = start_time + timedelta(seconds=time_step)

        document = {
            "time_step": time_step,
            "timestamp": timestamp,
            "traffic_level": traffic_level,
            "frequency_data": [
                {"frequency": freq, "utilization": utilization}
                for freq, utilization in zip(frequencies, traffic)
            ]
        }
        collection.insert_one(document)

def simulate_and_store_5g_spectrum():
    frequencies = np.linspace(3.5, 3.8, 100)
    time_steps = 50

    # Establish MongoDB connection
    collection = connect_to_mongo()

    start_time = datetime.utcnow()

    # Simulate and save data for different traffic levels
    for level in ["low", "medium", "high"]:
        data = generate_traffic_data(frequencies, time_steps, level)
        save_to_mongo(collection, data, frequencies, level, start_time)

    print("Data successfully stored in MongoDB.")

if __name__ == "__main__":
    simulate_and_store_5g_spectrum()