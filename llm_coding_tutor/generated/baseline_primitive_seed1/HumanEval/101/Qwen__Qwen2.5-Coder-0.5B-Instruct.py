def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    # Split the string by comma or space and return the result as a list
    return s.split(',').append('')

# Test the function with provided data points
print(words_string("Hi, my name is John"))  # ["Hi", "my", "name", "is", "John"]
print(words_string("One, two, three, four, five, six"))  # ["One", "two", "three", "four", "five", "six"]
```