import matplotlib.pyplot as plt
import numpy as np
import random

# Seed for reproducibility
random.seed('XYZ')

amount = 30
numbers = [random.randint(0, 1000) for _ in range(amount)]

def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        # Recursively sort the first and second halves
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)

        # Merge the sorted halves and visualize
        merge(arr, left, right, mid)
        plt.bar(list(range(amount)), arr, color=['blue' if left <= i <= right else 'grey' for i in range(amount)])
        plt.pause(0.01)
        plt.clf()

def merge(arr, left, right, mid):
    # Create temporary arrays to hold the left and right subarrays
    left_subarr = arr[left:mid + 1]
    right_subarr = arr[mid + 1:right + 1]

    # Initial indices for left, right, and merged subarrays
    i = 0  # Index for left_subarr
    j = 0  # Index for right_subarr
    k = left  # Index for the merged subarray

    # Merge the two subarrays back into arr
    while i < len(left_subarr) and j < len(right_subarr):
        if left_subarr[i] <= right_subarr[j]:
            arr[k] = left_subarr[i]
            i += 1
        else:
            arr[k] = right_subarr[j]
            j += 1
        k += 1

    # Copy any remaining elements from left_subarr, if any
    while i < len(left_subarr):
        arr[k] = left_subarr[i]
        i += 1
        k += 1

    # Copy any remaining elements from right_subarr, if any
    while j < len(right_subarr):
        arr[k] = right_subarr[j]
        j += 1
        k += 1

# Initialize interactive mode
plt.ion()
plt.figure(figsize=(10, 6))

# Initial plot of unsorted array
plt.bar(list(range(amount)), numbers, color='grey')
plt.title('Unsorted Array')
plt.show()
plt.pause(0.5)  # Pause to view the initial state

# Perform merge sort
merge_sort(numbers, 0, len(numbers) - 1)

# Final plot with sorted array
plt.bar(list(range(amount)), numbers, color='blue')
plt.title('Sorted Array')
plt.show()

# Disable interactive mode
plt.ioff()
