def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    # Check if the input is empty
    if not numbers:
        return (0, 1)

    # Calculate the sum
    total_sum = sum(numbers)

    # Calculate the product
    product = 1
    for num in numbers:
        product *= num

    return (total_sum, product)

# Example usage
print(sum_product([]))  # Output: (0,