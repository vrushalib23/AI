def selection(arr):
    n = len(arr)
    for i in range(n - 1):
        min = i
        for j in range(i + 1, n):
            if arr[j] < arr[min]:
                min = j
        # Swap after the inner loop completes
        arr[i], arr[min] = arr[min], arr[i]

arr1 = [24, 41, 14, 17, 6, 45]
selection(arr1)
print("Sorted array:", arr1)
