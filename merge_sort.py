import matplotlib.pyplot as plt
import numpy as np
import random

random.seed('XYZ')

amount = 30
numbers = [random.randint(0, 1000) for _ in range(amount)]

def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)

        merge(arr, left, right, mid)
        plt.bar(list(range(amount)), arr, color=['blue' if left <= i <= right else 'grey' for i in range(amount)])
        plt.pause(0.01)
        plt.clf()

def merge(arr, left, right, mid):
    left_subarr = arr[left:mid + 1]
    right_subarr = arr[mid + 1:right + 1]

    i = 0  
    j = 0  
    k = left  
    while i < len(left_subarr) and j < len(right_subarr):
        if left_subarr[i] <= right_subarr[j]:
            arr[k] = left_subarr[i]
            i += 1
        else:
            arr[k] = right_subarr[j]
            j += 1
        k += 1
    while i < len(left_subarr):
        arr[k] = left_subarr[i]
        i += 1
        k += 1
    while j < len(right_subarr):
        arr[k] = right_subarr[j]
        j += 1
        k += 1

plt.ion()
plt.figure(figsize=(10, 6))

plt.bar(list(range(amount)), numbers, color='grey')
plt.title('Unsorted Array')
plt.show()
plt.pause(0.5)  
merge_sort(numbers, 0, len(numbers) - 1)
plt.bar(list(range(amount)), numbers, color='blue')
plt.title('Sorted Array')
plt.show()
plt.ioff()
