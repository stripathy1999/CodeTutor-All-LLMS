from typing import List

def smallest_change(arr: List[int]) -> int:
    n = len(arr)
    changes = 0
    left, right = 0, n - 1
    
    while left < right:
        if arr[left]!= arr[right]:
            changes += 1
        left += 1
        right -= 1
    
    return changes

# check function to verify the correctness of the solution
def check_solution():
    assert smallest_change([1, 2, 3, 5, 4, 7, 9, 6]) == 4
    assert smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    assert smallest_change([1, 2, 3, 2, 1]) == 0
    print("All test cases passed!")

check_solution()
```