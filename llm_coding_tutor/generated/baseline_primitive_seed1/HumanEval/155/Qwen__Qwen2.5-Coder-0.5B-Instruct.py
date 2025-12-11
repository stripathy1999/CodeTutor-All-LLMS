def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even_count = 0
    odd_count = 0

    while num!= 0:
        digit = num % 10
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        num //= 10

    return (even_count, odd_count)

# check the function with provided data points
assert even_odd_count(-12) == (1, 1)
assert even_odd_count(123) == (1, 2)
assert even_odd_count(4567890) == (5, 5)
assert even_odd_count(13579) == (0, 5)
assert even_odd_count(0) == (1, 0)
assert even_odd_count(22) == (1, 1)
assert even_odd_count(333) == (3,