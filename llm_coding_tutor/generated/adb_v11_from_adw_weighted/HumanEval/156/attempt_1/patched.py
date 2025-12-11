def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    """
    # Define the Roman numeral symbols and their corresponding values
    roman_numerals = [
        ('m', 1000),
        ('cm', 900),
        ('d', 500),
        ('cd', 400),
        ('c', 100),
        ('xc', 90),
        ('l', 50),
        ('xl', 40),
        ('x', 10),
        ('ix', 9),
        ('v', 5),
        ('iv', 4),
        ('i', 1)
    ]
    
    # Initialize an empty string to build the Roman numeral
    result = ''
    
    # Iterate over each symbol and value pair
    for symbol, value in roman_numerals:
        # While number is greater than or equal to the current value
        while number >= value:
            # Append the symbol to the result
            result += symbol
            # Subtract the value from the number
            number -= value
    
    # Return