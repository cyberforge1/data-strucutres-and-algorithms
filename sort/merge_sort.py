# sort/merge_sort.py

# Merge sort algorithm for sorting an array in ascending order.
# A divide-and-conquer algorithm that recursively splits the array into halves,
# sorts each half, and merges them back together.
# Time Complexity:
# - Best, Worst, and Average Case: O(n log n)
# Space Complexity: O(n) (due to temporary arrays used during merging)

def merge_sort(arr):
    """Main merge sort function."""
    if len(arr) > 1:
        mid = len(arr) // 2

        # Divide the array into two halves
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively sort both halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the sorted halves
        merge(arr, left_half, right_half)

    return arr

def merge(arr, left_half, right_half):
    """Merge two sorted halves into a single sorted array."""
    i = j = k = 0

    # Merge until one of the halves is exhausted
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    # Copy any remaining elements from the left half
    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1

    # Copy any remaining elements from the right half
    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1
