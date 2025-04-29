import heapq

def heapsort(iterable):
    heap = []
    for value in iterable:
        heapq.heappush(heap, value)

    sorted_list = []
    while heap:
        sorted_list.append(heapq.heappop(heap))
    return sorted_list

# Example usage
data = [5, 3, 8, 4, 1, 9, 2]
sorted_data = heapsort(data)
print("Heap sorted:", sorted_data)
