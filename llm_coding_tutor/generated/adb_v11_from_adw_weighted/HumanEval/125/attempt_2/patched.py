from typing import List

def split_words(txt: str) -> List[str]:
    '''
    Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
    should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
    alphabet, ord('a') = 0, ord('b') = 1,... ord('z') = 25
    Examples
    split_words("Hello world!") ➞ ["Hello", "world!"]
    split_words("Hello,world!") ➞ ["Hello", "world!"]
    split_words("abcdef") == 3 
    '''
    # Split by whitespace
    words = txt.split()
    
    # Split by comma if no commas exist
    if ',' in txt:
        words = txt.split(',')
    
    # Split by odd order letters
    odd_order_letters = [chr(i) for i in range(ord('a'), ord('z')) if i % 2!= 0]
    words = [word for word in words if any(letter in odd_order_letters for letter in word)]
    
    return words