def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 *... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    """
    # Initialize the result list with zeros
    result = [0] * n
    
    # Loop through each number from 1 to n
    for i in range(1, n + 1):
        # Check if the current number is even
        if i % 2 == 0:
            # Calculate the factorial of the current number
            result[i - 1] = math.factorial(i)
        else:
            # Calculate the sum of numbers from 1 to the current number
            result[i - 1] = sum(range(1, i + 1))
    
    return result