# sort/quick_sort.py

# Quick sort algorithm for sorting an array in ascending order.
# A divide-and-conquer algorithm that partitions the array around a pivot element,
# placing smaller elements to the left and larger elements to the right, and recursively sorts the partitions.
# Time Complexity:
# - Best and Average Case: O(n log n)
# - Worst Case: O(n^2) (occurs when the pivot is poorly chosen, e.g., smallest or largest element)
# Space Complexity: O(log n) (for recursion stack in the average case)

def quick_sort(arr):
    """Main quick sort function."""
    _quick_sort(arr, 0, len(arr) - 1)
    return arr

def _quick_sort(arr, low, high):
    """Recursive helper function for quick sort."""
    if low < high:
        # Partition the array and get the pivot index
        pivot_index = partition(arr, low, high)
        # Recursively sort the left and right partitions
        _quick_sort(arr, low, pivot_index - 1)
        _quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    """Partition the array around a pivot element."""
    pivot = arr[high]  # Choose the last element as the pivot
    i = low - 1  # Pointer for the smaller element

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            # Swap elements
            arr[i], arr[j] = arr[j], arr[i]

    # Swap the pivot element with the element at i + 1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
