import numpy as np
from collections import deque

def detect_anomalies_real_time(data_stream, window_size=50, threshold=2, alpha=0.2):
    """
    Detect anomalies in a real-time data stream using Exponential Moving Average (EMA)
    and Z-Score. This function processes a stream of data points one at a time and flags
    those that deviate significantly from the expected range as anomalies.

    The algorithm works by maintaining an EMA for both the mean and variance (used to
    calculate standard deviation). It then computes the Z-Score for each new data point
    based on its deviation from the EMA and flags it as an anomaly if the Z-Score exceeds
    the defined threshold.

    Args:
        data_stream (iterable): A real-time data stream (e.g., a generator or list) of numerical data points.
        window_size (int, optional): The size of the window to store recent data points for initializing
            the EMA and variance. Defaults to 50.
        threshold (float, optional): The Z-Score threshold beyond which a data point is considered an anomaly.
            A higher threshold makes the detection stricter. Defaults to 2.
        alpha (float, optional): The smoothing factor for the EMA. Controls how much weight is given
            to new data points vs. previous EMA values. Defaults to 0.2.

    Yields:
        tuple: A tuple of (data_point, is_anomaly), where:
            - data_point (float): The current data point from the stream.
            - is_anomaly (bool): `True` if the data point is detected as an anomaly, `False` otherwise.

    Notes:
        - The `data_stream` should be an iterable that supplies data in real-time or in chunks.
        - Anomaly detection may take several data points to initialize since the EMA and variance
          need to stabilize over time.
    """
    data_window = deque(maxlen=window_size)
    ema = None
    ema_var = None  # EMA of variance

    for data_point in data_stream:
        data_window.append(data_point)
        is_anomaly = False

        if len(data_window) == window_size:
            if ema is None:
                # Initialize EMA with the first data point
                ema = np.mean(data_window)
                ema_var = np.var(data_window)

            # Update EMA and EMA variance
            # EMA = α * new data point + (1 − α) * previous EMA
            ema = alpha * data_point + (1 - alpha) * ema

            # EMA_var = α * (new data point − EMA) ^ 2 + (1 − α) * previous EMA_var
            ema_var = alpha * (data_point - ema) ** 2 + (1 - alpha) * ema_var

            # Compute the standard deviation from variance
            ema_std = np.sqrt(ema_var)

            # Calculate Z-Score
            z_score = (data_point - ema) / ema_std

            if abs(z_score) > threshold:
                is_anomaly = True  # Anomaly detected

        yield data_point, is_anomaly
