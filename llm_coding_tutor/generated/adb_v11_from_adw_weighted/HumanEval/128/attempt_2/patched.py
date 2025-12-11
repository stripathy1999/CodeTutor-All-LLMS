from typing import List, Optional

def prod_signs(arr: List[int]) -> Optional[int]:
    if not arr:
        return None
    
    product_sign = 1
    total_sum = 0
    
    for num in arr:
        if num == 0:
            return 0
        product_sign *= num
        total_sum += abs(num)
    
    return total_sum * product_sign