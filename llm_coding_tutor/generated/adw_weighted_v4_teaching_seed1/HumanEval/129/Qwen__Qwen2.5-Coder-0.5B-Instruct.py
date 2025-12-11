import heapq

def minPath(grid, k):
    # Initialize the grid with values 0 and count the occurrences of each value
    val_count = {}
    for row in grid:
        for col in row:
            if col > 0:
                val_count[col] = val_count.get(col, 0) + 1
    
    # Find the smallest value in the grid
    min_val = min(val_count.keys())
    
    # Create a priority queue based on the number of occurrences of each value
    pq = []
    for val in val_count:
        if val == min_val:
            heapq.heappush(pq, (val, val_count[val]))
    
    # Perform the k-th smallest path from the grid
    result = []
    while pq:
        val, count = heapq.heappop(pq)
        if count == k:
            result.append(val)
        else:
            for neighbor in [val - 1, val + 1]:
                if neighbor > 0 and neighbor < N:
                    heapq.heappush(pq, (neighbor, count + 1))
    
    return result