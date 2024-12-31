# sort/insertion_sort.py

# Insertion sort algorithm for sorting an array in ascending order.
# Builds the sorted array one element at a time by placing each element in its correct position.
# Time Complexity:
# - Best Case: O(n) (when the array is already sorted)
# - Worst Case: O(n^2) (when the array is sorted in reverse order)
# - Average Case: O(n^2)
# Space Complexity: O(1) (in-place sorting)

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]  # Element to be placed in the sorted portion
        j = i - 1

        # Move elements of the sorted portion that are greater than the key
        # to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Place the key in its correct position
        arr[j + 1] = key

    return arr
