from fractions import Fraction

def simplify(x, n):
    # Convert the inputs to Fraction objects
    num1, den1 = map(Fraction, x.split('/'))
    num2, den2 = map(Fraction, n.split('/'))
    
    # Simplify by dividing by the least common multiple (LCM)
    common_den = den1 * den2
    lcm = common_den * (num1.denom * num2.denom)
    simplified_num = num1 * num2 // lcm
    simplified_den = den1 * den2 // lcm
    
    # Check if the simplified fraction is a whole number
    return simplified_num.denominator == 1