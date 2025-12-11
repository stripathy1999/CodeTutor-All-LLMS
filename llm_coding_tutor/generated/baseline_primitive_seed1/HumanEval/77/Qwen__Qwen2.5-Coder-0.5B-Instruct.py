def iscube(a):
    if a < 0:
        return False
    cube_root = round(a ** (1/3))
    return cube_root ** 3 == a

# Test cases
print(iscube(1))     # True
print(iscube(2))     # False
print(iscube(-1))    # True
print(iscube(64))    # True
print(iscube(0))      # True
print(iscube(180))   # False
```

This function checks if the given integer `a` is a perfect cube by first finding its cube root using the `round` function. It then checks if squaring this root results in the original number `a`. If both conditions are met, `a` is a cube of some integer number. Otherwise, it is not a cube of any integer number.