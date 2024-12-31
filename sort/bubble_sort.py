# sort/bubble_sort.py

# Bubble sort algorithm for sorting an array in ascending order.
# Repeatedly steps through the list, compares adjacent elements, and swaps them if needed.
# Time Complexity:
# - Best Case: O(n) (when the array is already sorted)
# - Worst Case: O(n^2) (when the array is sorted in reverse order)
# - Average Case: O(n^2)
# Space Complexity: O(1) (in-place sorting)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False  # Track if any swaps occur during this pass
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap the elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no elements were swapped, the array is already sorted
        if not swapped:
            break
    return arr
