from typing import List

def make_a_pile(n: int) -> List[int]:
    piles = [n]
    while len(piles) < n:
        if n % 2 == 0:
            piles.append(piles[-1] + 2)
        else:
            piles.append(piles[-1] + 2)
    return piles

# Example usage:
print(make_a_pile(3))  # Output: [3, 5, 7]
```