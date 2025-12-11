def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    
    sum_result = sum(numbers)
    product_result = 1
    for num in numbers:
        product_result *= num
    
    return (sum_result, product_result)

# test cases
assert sum_product([]) == (0, 1)
assert sum_product([1, 2, 3, 4]) == (10, 24)
print("All tests passed successfully.")<|endanswer>