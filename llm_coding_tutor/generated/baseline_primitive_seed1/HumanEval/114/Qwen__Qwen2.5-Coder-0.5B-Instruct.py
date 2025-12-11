def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if not nums:
        return 0
    
    current_sum = min_sum = nums[0]
    
    for num in nums[1:]:
        current_sum = min(num, current_sum + num)
        min_sum = min(min_sum, current_sum)
    
    return min_sum

# check function to verify the correctness
def check_solution():
    assert minSubArraySum([2, 3, 4, 1, 2, 4]) == 1, "Test case 1 failed"
    assert minSubArraySum([-1, -2, -3]) == -6, "Test case 2 failed"
    assert minSubArraySum([5, 3, -2, 4, 1, 6, -3, 2]) == 1, "Test case 3 failed"