def total_match(lst1, lst2):
    '''
    Write a function that accepts two lists of strings and returns the list that has 
    total number of chars in the all strings of the list less than the other list.

    if the two lists have the same number of chars, return the first list.

    Examples
    total_match([], []) ➞ []
    total_match(['hi', 'admin'], ['hI', 'Hi']) ➞ ['hI', 'Hi']
    total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) ➞ ['hi', 'admin']
    total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) ➞ ['hI', 'hi', 'hi']
    total_match(['4'], ['1', '2', '3', '4', '5']) ➞ ['4']
    '''
    # Calculate the total number of characters in all strings of the first list
    total_chars_first_list = sum(len(s) for s in lst1)
    
    # Calculate the total number of characters in all strings of the second list
    total_chars_second_list = sum(len(s) for s in lst2)
    
    # Compare the total number of characters and return the appropriate list
    if total_chars_first_list < total_chars_second_list:
        return lst1
    else:
        return lst2