import numpy as np
import random

# Constants and parameters
BANDWIDTH = 1000  # MHz, total bandwidth available for 6G
NUM_USERS = 10  # Number of users connected to the network
TRAFFIC_LOAD = [random.uniform(1, 10) for _ in range(NUM_USERS)]  # Random traffic load per user in Gbps
LATENCY_BASELINE = 1  # ms baseline latency without congestion

# Spectrum Utilization: Amount of bandwidth used by each user (MHz)
def calculate_spectrum_utilization(bandwidth, traffic_load):
    utilization = [min(bandwidth * (load / sum(traffic_load)), bandwidth) for load in traffic_load]
    return utilization

# QoS: Measure latency and throughput for each user based on traffic load and bandwidth
def calculate_qos(utilization, traffic_load):
    latencies = []
    throughputs = []

    for i in range(len(utilization)):
        # Latency increases if traffic exceeds available spectrum
        if traffic_load[i] > utilization[i]:
            latency = LATENCY_BASELINE * (traffic_load[i] / utilization[i])
        else:
            latency = LATENCY_BASELINE
        
        # Throughput is the minimum of what the user demands or what they can actually get
        throughput = min(traffic_load[i], utilization[i])
        
        latencies.append(latency)
        throughputs.append(throughput)

    return latencies, throughputs

# Main simulation function
def simulate_6g_network():
    utilization = calculate_spectrum_utilization(BANDWIDTH, TRAFFIC_LOAD)
    latencies, throughputs = calculate_qos(utilization, TRAFFIC_LOAD)

    print(f"{'User':<5} {'Traffic Load (Gbps)':<20} {'Utilization (MHz)':<20} {'Latency (ms)':<15} {'Throughput (Gbps)':<20}")
    print("-" * 80)

    for i in range(NUM_USERS):
        print(f"{i+1:<5} {TRAFFIC_LOAD[i]:<20.2f} {utilization[i]:<20.2f} {latencies[i]:<15.2f} {throughputs[i]:<20.2f}")

# Running the simulation
simulate_6g_network()import numpy as np
import random

# Constants and parameters
BANDWIDTH = 1000  # MHz, total bandwidth available for 6G
NUM_USERS = 10  # Number of users connected to the network
TRAFFIC_LOAD = [random.uniform(1, 10) for _ in range(NUM_USERS)]  # Random traffic load per user in Gbps
LATENCY_BASELINE = 1  # ms baseline latency without congestion

# Spectrum Utilization: Amount of bandwidth used by each user (MHz)
def calculate_spectrum_utilization(bandwidth, traffic_load):
    utilization = [min(bandwidth * (load / sum(traffic_load)), bandwidth) for load in traffic_load]
    return utilization

# QoS: Measure latency and throughput for each user based on traffic load and bandwidth
def calculate_qos(utilization, traffic_load):
    latencies = []
    throughputs = []

    for i in range(len(utilization)):
        # Latency increases if traffic exceeds available spectrum
        if traffic_load[i] > utilization[i]:
            latency = LATENCY_BASELINE * (traffic_load[i] / utilization[i])
        else:
            latency = LATENCY_BASELINE
        
        # Throughput is the minimum of what the user demands or what they can actually get
        throughput = min(traffic_load[i], utilization[i])
        
        latencies.append(latency)
        throughputs.append(throughput)

    return latencies, throughputs

# Main simulation function
def simulate_6g_network():
    utilization = calculate_spectrum_utilization(BANDWIDTH, TRAFFIC_LOAD)
    latencies, throughputs = calculate_qos(utilization, TRAFFIC_LOAD)

    print(f"{'User':<5} {'Traffic Load (Gbps)':<20} {'Utilization (MHz)':<20} {'Latency (ms)':<15} {'Throughput (Gbps)':<20}")
    print("-" * 80)

    for i in range(NUM_USERS):
        print(f"{i+1:<5} {TRAFFIC_LOAD[i]:<20.2f} {utilization[i]:<20.2f} {latencies[i]:<15.2f} {throughputs[i]:<20.2f}")

# Running the simulation
simulate_6g_network()
