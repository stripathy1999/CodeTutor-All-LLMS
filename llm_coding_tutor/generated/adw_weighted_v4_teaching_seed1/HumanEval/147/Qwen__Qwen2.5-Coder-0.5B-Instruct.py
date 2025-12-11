def get_max_triples(n):
    """
    You are given a positive integer n. You have to create an integer array a of length n.
        For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
        Return the number of triples (a[i], a[j], a[k]) of a where i < j < k, 
    and a[i] + a[j] + a[k] is a multiple of 3.

    Example :
        Input: n = 5
        Output: 1
        Explanation: 
        a = [1, 3, 7, 13, 21]
        The only valid triple is (1, 7, 13).
    """
    # Initialize the array with the first three multiples of 3
    a = [3 * i for i in range(1, 4)]
    
    # Use the binary search algorithm to find all triples that sum to 3k (where k is a multiple of 3)
    left, right = 0, len(a) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if a[mid] + a[left] == 3 * mid:
            return 1
        elif a[mid] + a[left] < 3 * mid:
            left += 1
        else:
            right -= 1
    
    return 0