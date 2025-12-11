def below_threshold(l: list, t: int):
    # Iterate over each number in the list
    for num in l:
        # Check if the number is below the threshold t
        if num < t:
            return False
    # If no number is below the threshold, return True
    return True