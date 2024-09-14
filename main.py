import time
from anomaly_detection import detect_anomalies_real_time
from data_stream import generate_data_stream_real_time
from visualize import visualize_data

if __name__ == "__main__":
    data = []
    anomalies = []

    data_stream = generate_data_stream_real_time(stream_length=1000, delay=0.1)
    anomaly_detector = detect_anomalies_real_time(data_stream, window_size=50, threshold=2)

    for data_point, is_anomaly in anomaly_detector:
        data.append(data_point)

        if is_anomaly:
            # add the data point index into the anomalies list
            anomalies.append(len(data) - 1)

        # Visualize data in real-time, but less frequently
        if len(data) % 50 == 0:  # Update plot every 50 data points
            visualize_data(data, anomalies)

        time.sleep(0.01)
