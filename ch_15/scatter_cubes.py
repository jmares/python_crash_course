import matplotlib.pyplot as plt

x_values = range(1, 5000)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
#ax.scatter(x_values, y_values, c=(0.8, 0, 0.8), s=10)
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.turbo, s=10)

# Set chart title and label axes
ax.set_title("Cube Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

# Set size of tick labels
ax.tick_params(axis="both", which='major', labelsize=14)

# Set range for each axis

ax.axis([0, 5000, 0, 125000000000])

plt.savefig('cubes_plot.png', bbox_inches='tight')
plt.show()