import matplotlib.pyplot as plt

# Sample data
x = [2, 4, 6, 8, 10, 12, 14, 16, 18]
y = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Create scatter plot
plt.scatter(x, y)

# Add title and labels
plt.title('XY Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Show plot
plt.show()