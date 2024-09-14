import matplotlib.pyplot as plt


def initialize_plot():
    """Initializes the plot and returns the figure, axes, and plot handles."""
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlabel('Time')
    ax.set_ylabel('Value')
    ax.set_title('Real-time Data Stream with Anomalies')

    # Create empty line plot and scatter plot
    line, = ax.plot([], [], label='Data Stream', color='blue')
    scatter = ax.scatter([], [], color='red', label='Anomalies')

    ax.legend()

    return fig, ax, line, scatter


def update_plot(ax, line, scatter, data, anomalies):
    """Updates the plot with new data and anomalies."""
    # Update line plot with new data
    line.set_data(range(len(data)), data)

    # Update scatter plot with anomalies
    plt.scatter([i for i in range(len(data)) if i in anomalies], [data[i] for i in anomalies], color='red', label='Anomalies')

    ax.relim()  # Recompute the limits of the plot
    ax.autoscale_view()  # Rescale the axes to fit new data

    plt.draw()
    plt.pause(0.01)
