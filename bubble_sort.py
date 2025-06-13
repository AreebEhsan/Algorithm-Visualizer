import matplotlib.pyplot as plt
import numpy as np

amount = 20
lst = np.random.randint(0, 100, amount)
x = np.arange(amount) 

plt.ion() 

n = len(lst)
for i in range(n):
    for j in range(n - i - 1): 
        colors = ['blue' if k < n - i - 1 else 'green' for k in range(n)]

        plt.bar(x, lst, color=colors)
        plt.pause(0.1) 

        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
        plt.clf() 

plt.ioff()
plt.bar(x, lst, color='green')
plt.title('Sorted List')
plt.show()
