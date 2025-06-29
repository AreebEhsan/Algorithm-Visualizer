def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    def partition(low, high, arr):
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
    def quicksort_helper(low: int, high: int, arr: list[int]) -> None:
        if low < high:
            pi = partition(low, high, arr)
            quicksort_helper(low, pi - 1, arr)
            quicksort_helper(pi + 1, high, arr)
    
    result = arr.copy()
    quicksort_helper(0, len(result) - 1, result)
    return result