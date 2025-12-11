def int_to_mini_roman\(number\):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase\.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman\(19\) == 'xix'
    >>> int_to_mini_roman\(152\) == 'clii'
    >>> int_to_mini_roman\(426\) == 'cdxxvi'
    """
    # Define the Roman numeral symbols and their corresponding values
    roman_numerals = \[
        \('M', 1000\),
        \('CM', 900\),
        \('D', 500\),
        \('CD', 400\),
        \('C', 100\),
        \('XC', 90\),
        \('L', 50\),
        \('XL', 40\),
        \('X', 10\),
        \('IX', 9\),
        \('V', 5\),
        \('IV', 4\),
        \('I', 1\)
    \]
    
    # Initialize the result string
    result = ''
    
    # Iterate over each symbol and its value
    for symbol, value in roman_numerals:
        # While the number is greater than or equal to the current symbol's value
        while number >= value:
            # Append the symbol to the result string
            result \+= symbol
            # Subtract the symbol's value from the number
            number -= value
    
    return