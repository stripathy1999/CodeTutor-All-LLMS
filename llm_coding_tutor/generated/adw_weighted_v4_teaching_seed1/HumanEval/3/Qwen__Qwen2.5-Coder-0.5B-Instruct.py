from typing import List


def below_zero(operations: List[int]) -> bool:
    """ Detects if the balance of an account falls below zero at any point.

    Parameters:
    operations (List[int]): A list of integers representing deposit and withdrawal operations.

    Returns:
    bool: True if the balance falls below zero at any point, False otherwise.
    """
    balance = 0
    for operation in operations:
        balance += operation
        if balance < 0:
            return True
    return False