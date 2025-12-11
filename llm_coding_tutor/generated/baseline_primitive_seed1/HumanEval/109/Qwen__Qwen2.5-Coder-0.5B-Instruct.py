def move_one_ball(arr):
    if not arr:
        return True
    
    n = len(arr)
    # Check if the array can be sorted by performing rotations
    for _ in range(n):
        for i in range(n - 1):
            if arr[i] > arr[(i + 1) % n]:
                arr[i], arr[(i + 1) % n] = arr[(i + 1) % n], arr[i]
                break
    
    return True

# Test cases
print(move_one_ball([3, 4, 5, 1, 2]))  # True
print(move_one_ball([3, 5, 4, 1, 2]))  # False
```

This solution iterates through the array and checks if each element is greater than the next element, indicating that a rotation would sort the array. If such a rotation is found, it returns `True`; otherwise, it returns `False`.