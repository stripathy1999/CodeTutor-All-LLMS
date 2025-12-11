def add(lst):
    # Initialize sum to 0
    sum = 0
    
    # Iterate over the list with index
    for i in range(len(lst)):
        # Check if the index is odd
        if i % 2!= 0:
            # Check if the element is even
            if lst[i] % 2 == 0:
                # Add the even element to the sum
                sum += lst[i]
    
    # Return the final sum
    return sum

# Test cases
print(add([4, 2, 6, 7]))  # Output: 2
print(add([1, 3, 5, 7, 9]))  # Output: 18
print(add([2, 4, 6, 8, 10]))  # Output: 0
```