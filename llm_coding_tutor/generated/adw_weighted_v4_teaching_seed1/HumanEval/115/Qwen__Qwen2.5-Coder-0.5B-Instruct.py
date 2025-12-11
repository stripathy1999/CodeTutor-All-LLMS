def max_fill(grid, capacity):
    # Initialize the number of buckets
    buckets = [0] * len(grid[0])
    
    # Iterate through each well
    for well in grid:
        # Calculate the amount of water needed to fill the well
        water_needed = sum(well)
        
        # Update the number of buckets required
        for i in range(len(buckets)):
            if buckets[i] + water_needed <= capacity:
                buckets[i] += water_needed
                break
    
    # Return the total number of times buckets need to be lowered
    return sum(buckets)

# Example usage
grid1 = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
capacity1 = 1
print(max_fill(grid1, capacity1))  # Output: 6

grid2 = [[0,0