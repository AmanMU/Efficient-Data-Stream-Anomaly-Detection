import time

from matplotlib import pyplot as plt

from anomaly_detection import detect_anomalies_real_time
from data_stream import generate_data_stream_real_time
from visualize import initialize_plot, update_plot

if __name__ == "__main__":
    data = []
    anomalies = []

    # Initialize the plot
    fig, ax, line, scatter = initialize_plot()

    data_stream = generate_data_stream_real_time(stream_length=1000, delay=0.1)
    anomaly_detector = detect_anomalies_real_time(data_stream)

    for data_point, is_anomaly in anomaly_detector:
        data.append(data_point)

        if is_anomaly:
            anomalies.append(len(data) - 1)

        # Update the plot in real-time
        update_plot(ax, line, scatter, data, anomalies)

        # Simulate real-time update
        time.sleep(0.01)

    plt.show()  # Keep the final plot open after the loop ends
