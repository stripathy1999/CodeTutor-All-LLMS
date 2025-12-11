def double_the_difference(lst):
    # Initialize the sum to 0
    total_sum = 0
    
    # Flag to check if there are any negative numbers
    has_negative = False
    
    # Flag to check if there are any odd numbers
    has_odd = False
    
    # Iterate through each number in the list
    for num in lst:
        # Check if the number is an integer and positive
        if isinstance(num, int) and num > 0:
            # Check if the number is odd
            if num % 2!= 0:
                # Calculate the square of the number
                square = num ** 2
                # Add the square to the total sum
                total_sum += square
                # Flag for negative numbers
                has_negative = True
                # Flag for odd numbers
                has_odd = True
    
    # If there were no negative numbers or odd numbers, return 0
    if not has_negative and not has_odd:
        return 0
    
    # Return the total sum
    return total_sum

# Test cases
print(double_the_difference([1, 3, 2, 0]))  # Output: 10
print(double_the_difference([-1, -