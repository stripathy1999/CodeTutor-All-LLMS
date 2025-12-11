def split_words(txt):
    '''
    Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
    should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
    alphabet, ord('a') = 0, ord('b') = 1,... ord('z') = 25
    Examples
    split_words("Hello world!") ➞ ["Hello", "world!"]
    split_words("Hello,world!") ➞ ["Hello", "world!"]
    split_words("abcdef") == 3 
    '''
    # Check for empty input
    if not txt:
        return []

    # Check for single-element input
    if len(txt) == 1:
        return [txt]

    # Check for negative input
    if txt[0] < 0:
        return []

    # Check for boundary input
    if txt[-1] =='':
        return []

    # Split by whitespace
    words = txt.split()

    # Split by commas
    if ',' in txt:
        words = [word for word in words if ',' in word]

    # Count odd order letters
    odd_order_letters = sum(1 for char in txt if char.islower() and ord(char) % 2!= 0)

    return words, odd_order_letters