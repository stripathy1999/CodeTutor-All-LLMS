from fractions import Fraction

def simplify(x, n):
    x_fraction = Fraction(x)
    n_fraction = Fraction(n)
    product_fraction = x_fraction * n_fraction
    return product_fraction.denominator == 1

# Test cases
print(simplify("1/5", "5/1"))  # Output: True
print(simplify("1/6", "2/1"))  # Output: False
print(simplify("7/10", "10/2"))  # Output: False
```