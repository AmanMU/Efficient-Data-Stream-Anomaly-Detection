import time
import numpy as np

def generate_data_stream_real_time(stream_length=1000, delay=0.01):
    time_index = 0
    while time_index < stream_length:
        # Regular pattern: Sine wave + seasonal trend + noise
        # y = A * sin(B * t + C) + A * cos(B * t + C) where A amplitude, B frequency scaling factor, t time, C starting point
        # The sine wave creates more rapid oscillations between -10 and 10 with a frequency controlled by the factor 0.05.
        # The cosine wave adds a more gradual oscillation between -5 and 5, with a much lower frequency controlled by the factor 0.01.
        data_point = 10 * np.sin(time_index * 0.05) + 5 * np.cos(time_index * 0.01)

        # np.random.normal(0, 0.5) generates a random value with a mean of 0 and a standard deviation of 0.5.
        # This simulates real-world data, where measurements often contain noise.
        data_point += np.random.normal(0, 0.5)

        # Randomly inject anomalies (spikes)
        # np.random.random() generates a random float between 0 and 1. If this value is greater than 0.98, the condition is satisfied, which happens with a 2% probability.
        # data_point += np.random.uniform(15, 30) adds a random spike to the data point.
        # The spike is uniformly distributed between 15 and 30 units, creating an anomaly much larger than the regular pattern.
        if np.random.random() > 0.98:
            data_point += np.random.uniform(15, 30)

        # The yield keyword is used to return the generated data_point without stopping the function execution.
        # This makes the function a generator, allowing it to produce data points one by one and pause between each point, simulating real-time streaming behavior.
        yield data_point
        time_index += 1
        time.sleep(delay)