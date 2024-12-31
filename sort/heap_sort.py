# sort/heap_sort.py

# Heap sort algorithm for sorting an array in ascending order.
# Uses a binary heap to repeatedly extract the largest (or smallest) element.
# Time Complexity:
# - Best, Worst, and Average Case: O(n log n)
# Space Complexity: O(1) (in-place sorting)

def heapify(arr, n, i):
    """Helper function to maintain the heap property."""
    largest = i  # Assume the root is the largest
    left = 2 * i + 1  # Left child index
    right = 2 * i + 2  # Right child index

    # Check if left child exists and is greater than the root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is greater than the largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If the largest is not the root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    """Main heap sort function."""
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from the heap
    for i in range(n - 1, 0, -1):
        # Move the current root (largest) to the end
        arr[0], arr[i] = arr[i], arr[0]
        # Heapify the reduced heap
        heapify(arr, i, 0)

    return arr
