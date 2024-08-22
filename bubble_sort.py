import matplotlib.pyplot as plt
import numpy as np

amount = 20
lst = np.random.randint(0, 100, amount)
x = np.arange(amount)  # Adjusted x to match the length of lst

plt.ion()  # Turn on interactive mode for dynamic plotting

n = len(lst)
for i in range(n):
    for j in range(n - i - 1):  # Adjusted loop to avoid index error
        # Color-coding elements: blue for unsorted, green for sorted
        colors = ['blue' if k < n - i - 1 else 'green' for k in range(n)]

        plt.bar(x, lst, color=colors)
        plt.pause(0.1)  # Increased pause to make the sorting process visible

        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
        plt.clf()  # Clear the figure for the next plot

plt.ioff()  # Turn off interactive mode
plt.bar(x, lst, color='green')  # Final plot with sorted list
plt.title('Sorted List')
plt.show()
