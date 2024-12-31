# search/binary_search.py

# Binary search algorithm to find the index of a target element in a sorted array.
# Works by repeatedly dividing the search interval in half. 
# Time Complexity: O(log n), Space Complexity: O(1). Returns -1 if the target is not found.

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        # Compare the middle element with the target
        if arr[mid] == target:
            return mid  # Target found at index `mid`
        elif arr[mid] < target:
            low = mid + 1  # Search in the right half
        else:
            high = mid - 1  # Search in the left half

    return -1
