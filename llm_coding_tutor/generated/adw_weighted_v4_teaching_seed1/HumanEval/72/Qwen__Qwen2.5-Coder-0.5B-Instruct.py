def will_it_fly(q, w):
    '''
    Write a function that returns True if the object q will fly, and False otherwise.
    The object q will fly if it's balanced (it is a palindromic list) and the sum of its elements is less than or equal the maximum possible weight w.

    Example:
    will_it_fly([1, 2], 5) ➞ False 
    # 1+2 is less than the maximum possible weight, but it's unbalanced.

    will_it_fly([3, 2, 3], 1) ➞ False
    # it's balanced, but 3+2+3 is more than the maximum possible weight.

    will_it_fly([3, 2, 3], 9) ➞ True
    # 3+2+3 is less than the maximum possible weight, and it's balanced.

    will_it_fly([3], 5) ➞ True
    # 3 is less than the maximum possible weight, and it's balanced.
    '''

    # Check if the object is a palindrome
    if q!= q[::-1]:
        return False

    # Initialize variables to keep track of the sum of elements and the maximum weight
    total_weight = 0
    max_weight = w

    # Iterate through each element in the list
    for element in q:
        total_weight += element
        max_weight = max(max_weight, element)

    # Check if the sum of elements is less than or equal to the maximum weight
    return total_weight <= max_weight