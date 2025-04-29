def heapify(arr, n, i):
    largest = i        # Initialize largest as root
    left = 2 * i + 1   # left child
    right = 2 * i + 2  # right child

    # See if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # See if right child exists and is greater than current largest
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Change root if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        heapify(arr, n, largest)

def heapsort(arr):
    n = len(arr)

    # Build a maxheap (rearrange array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)

# Example usage
data = [5, 3, 8, 4, 1, 9, 2]
heapsort(data)
print("Heap sorted:", data)
