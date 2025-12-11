def solve(N):
    # Convert the integer to a string to iterate over each digit
    str_N = str(N)
    
    # Initialize the total sum of digits
    total_sum = 0
    
    # Iterate over each character in the string representation of N
    for digit in str_N:
        # Convert the character back to an integer
        num = int(digit)
        # Add the digit to the total sum
        total_sum += num
    
    # Convert the total sum to binary and return it
    return bin(total_sum)[2:]

# Example usage
print(solve(1000))  # Output: "1"
print(solve(150))   # Output: "110"
print(solve(147))   # Output: "1100"