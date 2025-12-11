from typing import List, Optional

def prod_signs(arr: List[int]) -> Optional[int]:
    if not arr:
        return None
    
    product_sign = 1
    total_magnitude = 0
    
    for num in arr:
        if num == 0:
            return 0
        elif num < 0:
            product_sign *= -1
        total_magnitude += abs(num)
    
    return total_magnitude * product_sign