import numpy as np
import matplotlib.pyplot as plt

# Unsorted input data
unsorted_input_data_demo = {
    "Cluster 1": 450,
    "Cluster 2": 1500,
    "Cluster 3": 600,
    "Cluster 4": 400,
    "Cluster 5": 390,
    "Cluster 6": 900
}

# Sort the data by values
sorted_data = dict(sorted(unsorted_input_data_demo.items(), key=lambda item: item[1]))

# Extract sorted keys and values
names = list(sorted_data.keys())
values = list(sorted_data.values())

# Extract sorted k-values and values
k_values = np.arange(1, len(values) + 1)
value_array = np.array(values)

# Correct diagonal line calculation
x1, y1 = 0, value_array[0]  # Starting at the "virtual" 0th cluster for alignment
x2, y2 = len(k_values) - 1, value_array[-1]  # Last cluster index aligns with last value

# Line vector recalculation
line_vec = np.array([x2 - x1, y2 - y1])
line_vec_norm = line_vec / np.linalg.norm(line_vec)

# Calculate distances from each point to the diagonal line
distances = []
for i in range(len(k_values)):
    point = np.array([i, value_array[i]])  # Use the index of k_values
    point_vec = point - np.array([x1, y1])
    proj_of_point = point_vec.dot(line_vec_norm)
    proj_point = proj_of_point * line_vec_norm
    dist = np.linalg.norm(point_vec - proj_point)
    distances.append(dist)

# Find the elbow point
elbow_index = np.argmax(distances)

# Plot the Elbow Criterion
plt.figure(figsize=(8, 5))
plt.plot(names, value_array, 'bo-', label='Values (Sorted)')
plt.plot(names, value_array, 'b-')  # Line connecting points
plt.axline((x1, y1), (x2, y2), color='r', linestyle='--', label='Connecting Line')
plt.scatter(names[elbow_index], value_array[elbow_index], color='green', s=100, label='Elbow Point', zorder=5)

# Annotate the elbow point
plt.annotate(f"Elbow ({names[elbow_index]}, {value_array[elbow_index]})",
             xy=(names[elbow_index], value_array[elbow_index]),
             xytext=(elbow_index + 1, value_array[elbow_index] + 100),
             arrowprops=dict(facecolor='black', arrowstyle="->"))

plt.title('Elbow Criterion with Corrected Diagonal Line')
plt.xlabel('Clusters')
plt.ylabel('Values')
plt.legend()
plt.grid(True)
plt.show()
