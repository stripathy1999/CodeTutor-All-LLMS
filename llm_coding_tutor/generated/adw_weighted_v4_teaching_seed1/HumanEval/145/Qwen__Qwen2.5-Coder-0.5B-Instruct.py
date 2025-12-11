def order_by_points(nums):
    """
    Sorts the given list of integers in ascending order according to the sum of their digits.
    If there are several items with similar sum of their digits, orders them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    # Helper function to calculate the sum of digits of a number
    def digit_sum(n):
        return sum(int(digit) for digit in str(abs(n)))

    # Sort the list using a custom key that first sorts by digit sum, then by index
    sorted_nums = sorted(nums, key=lambda x: (digit_sum(x), nums.index(x)))
    return sorted_nums

# Check function