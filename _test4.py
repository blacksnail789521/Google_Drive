import matplotlib.pyplot as plt
import numpy as np

# Using two separate dictionaries for two tools
tabular_times_dict = {
    "Tool 1": 5,
    "Tool 2": 7,
}

time_series_times_dict = {
    "Tool 1": 15,
    "Tool 2": 17,
}

# Extracting tools and running times
tools = list(tabular_times_dict.keys())
tabular_times = list(tabular_times_dict.values())
time_series_times = list(time_series_times_dict.values())

# Create a plot
plt.figure(figsize=(8, 5))
x = np.arange(len(tools))  # Position of bars on the x-axis

# Bar chart for the running times
bar_width = 0.35
plt.bar(x - bar_width/2, tabular_times, width=bar_width, label='Tabular Model', color='blue')
plt.bar(x + bar_width/2, time_series_times, width=bar_width, label='Time Series Model', color='orange')

# Adding labels, title, and legend
plt.title('Running Time Comparison for Two Tools')
plt.xlabel('Tools')
plt.ylabel('Running Time (seconds)')
plt.xticks(x, tools)
plt.legend()

# Show the plot
plt.tight_layout()
plt.show()
