def specialFilter(nums):
    count = 0
    for num in nums:
        if num > 10 and is_all_odd_digits(num):
            count += 1
    return count

def is_all_odd_digits(n):
    while n > 0:
        digit = n % 10
        if digit % 2 == 0:
            return False
        n //= 10
    return True

# Test cases
print(specialFilter([15, -73, 14, -15]))  # Output: 1
print(specialFilter([33, -2, -3, 45, 21, 109]))  # Output: 2
```