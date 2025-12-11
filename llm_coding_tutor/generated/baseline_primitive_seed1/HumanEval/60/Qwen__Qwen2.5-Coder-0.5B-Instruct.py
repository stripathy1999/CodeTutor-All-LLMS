def sum_to_n(n: int) -> int:
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Test cases
assert sum_to_n(30) == 465, "Test case 1 failed"
assert sum_to_n(100) == 5050, "Test case 2 failed"
assert sum_to_n(5) == 15, "Test case 3 failed"
assert sum_to_n(10) == 55, "Test case 4 failed"
assert sum_to_n(1) == 1, "Test case 5 failed"
print("All test cases passed!")<|end>