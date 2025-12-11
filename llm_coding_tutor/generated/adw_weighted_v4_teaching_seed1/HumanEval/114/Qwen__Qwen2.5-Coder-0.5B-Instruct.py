def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    
    Parameters:
    nums (list): A list of integers.
    
    Returns:
    int: The minimum sum of any non-empty sub-array of nums.
    """
    if not nums:
        return 0
    
    min_sum = float('inf')
    current_sum = 0
    
    for num in nums:
        current_sum += num
    
        if current_sum < min_sum:
            min_sum = current_sum
        
        if current_sum > 0:
            current_sum = 0
    
    return min_sum