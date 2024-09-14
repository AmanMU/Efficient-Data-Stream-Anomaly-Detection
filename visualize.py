import matplotlib.pyplot as plt

def visualize_data(data, anomalies):
    """Visualizes the data stream and anomalies."""
    plt.figure(figsize=(10, 6))
    plt.plot(data, label='Data Stream', color='blue')
    plt.scatter([i for i in range(len(data)) if i in anomalies], [data[i] for i in anomalies], color='red', label='Anomalies')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.legend()
    plt.draw()
    plt.pause(0.1)  # Pause to update the plot