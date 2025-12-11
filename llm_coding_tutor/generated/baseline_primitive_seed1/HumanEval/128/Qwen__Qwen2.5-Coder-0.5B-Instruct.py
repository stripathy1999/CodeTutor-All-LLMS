def prod_signs(arr):
    if not arr:
        return None
    
    sign_product = 1
    total_sum = 0
    
    for num in arr:
        sign_product *= int(num)  # Multiply the sign product by the number's absolute value
        if num < 0:
            total_sum += sign_product  # Add the product of all signs to the total sum
    
    return total_sum

# Test cases
assert prod_signs([1, 2, 2, -4]) == -9
assert prod_signs([0, 1]) == 0
assert prod_signs([]) == None
```