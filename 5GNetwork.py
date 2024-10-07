import random
import numpy as np

# Constants
TOTAL_BANDWIDTH = 1000  # MHz total bandwidth across all RUs
NUM_RUS = 3  # Number of Radio Units (RUs)
NUM_USERS_PER_RU = 10  # Users connected to each RU
TRAFFIC_LOAD = np.array([random.uniform(1, 10) for _ in range(NUM_RUS * NUM_USERS_PER_RU)])  # Convert to NumPy array

# Capacity and latency per layer
RU_CAPACITY = TOTAL_BANDWIDTH / NUM_RUS  # Bandwidth per RU
DU_CAPACITY = TOTAL_BANDWIDTH * 0.8  # 80% of total capacity allocated to Distributed Units
CU_CAPACITY = TOTAL_BANDWIDTH * 0.6  # 60% of total capacity allocated to Centralized Units

LATENCY_RU = 1  # Latency at Radio Unit (ms)
LATENCY_DU = 2  # Latency at Distributed Unit (ms)
LATENCY_CU = 5  # Latency at Centralized Unit (ms)

# Function to calculate spectrum utilization across RUs
def calculate_spectrum_utilization_ru(traffic_load, ru_capacity):
    total_load = sum(traffic_load)
    ru_utilization = [min(load / total_load * ru_capacity, ru_capacity) for load in traffic_load]
    return ru_utilization

# Function to calculate QoS (latency and throughput) considering Open RAN structure
def calculate_qos_open_ran(ru_utilization, traffic_load, ru_capacity):
    latencies = []
    throughputs = []

    for i in range(len(ru_utilization)):
        # Calculate latency based on whether the traffic exceeds the RU, DU, or CU capacity
        latency = LATENCY_RU + LATENCY_DU + LATENCY_CU  # Start with baseline latencies for each layer

        # Adjust latency if traffic load exceeds RU, DU, or CU capacity
        if traffic_load[i] > RU_CAPACITY:
            latency += LATENCY_RU  # Increased delay at RU due to congestion
        if traffic_load[i] > DU_CAPACITY:
            latency += LATENCY_DU  # Increased delay at DU
        if traffic_load[i] > CU_CAPACITY:
            latency += LATENCY_CU  # Increased delay at CU

        # Throughput is the minimum of traffic demand or what the network can support
        throughput = min(traffic_load[i], ru_utilization[i])

        latencies.append(latency)
        throughputs.append(throughput)

    return latencies, throughputs

# Simulation function to distribute traffic across RUs and simulate Open RAN QoS
def simulate_open_ran_network():
    # Split traffic into RUs
    ru_traffic_load = np.split(TRAFFIC_LOAD, NUM_RUS)

    for ru_id, traffic in enumerate(ru_traffic_load):
        print(f"\n--- RU {ru_id + 1} Simulation ---")
        ru_utilization = calculate_spectrum_utilization_ru(traffic, RU_CAPACITY)
        latencies, throughputs = calculate_qos_open_ran(ru_utilization, traffic, RU_CAPACITY)

        print(f"{'User':<5} {'Traffic Load (Gbps)':<20} {'Utilization (MHz)':<20} {'Latency (ms)':<15} {'Throughput (Gbps)':<20}")
        print("-" * 80)

        for i in range(NUM_USERS_PER_RU):
            print(f"{i + 1:<5} {traffic[i]:<20.2f} {ru_utilization[i]:<20.2f} {latencies[i]:<15.2f} {throughputs[i]:<20.2f}")

# Running the simulation
simulate_open_ran_network()
