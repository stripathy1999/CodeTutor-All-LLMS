def minPath(grid, k):
    # Initialize the result with the first row and column
    res = [[grid[0][j]] + [grid[j][0]] for j in range(len(grid[0]))]
    
    # Iterate through the grid starting from the second element
    for i in range(1, len(grid)):
        for j in range(1, len(grid[0])):
            # Find the minimum value between the current cell and its neighbors
            res[i].append(min(res[i - 1][j], res[i][j - 1]))
    
    return res[-k:]

# Example usage:
print(minPath([[1,2,3],[4,5,6],[7,8,9]], 3))  # Output: [1, 2, 1]
print(minPath([[5,9,3],[4,1,6],[7,8,2]], 1))   # Output: [1]```