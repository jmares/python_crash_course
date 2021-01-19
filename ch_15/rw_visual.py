import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    # Make a random walk

    rw = RandomWalk(50_000)
    rw.fill_walk()

    # Plot the points in the walk

    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15,9))
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.cool, edgecolors='none' ,s=1)
    # Emphasize first and last points
    ax.scatter(0, 0, c='navy', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='purple', edgecolors='none', s=100)
    # Remove the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.savefig('rw.png', bbox_inches='tight')
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break