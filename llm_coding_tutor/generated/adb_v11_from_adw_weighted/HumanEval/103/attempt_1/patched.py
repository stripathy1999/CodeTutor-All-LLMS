import math

def rounded_avg(n, m):
    if n > m:
        return -1
    
    total_sum = sum(range(n, m + 1))
    count = m - n + 1
    
    rounded_avg = round(total_sum / count)
    
    return bin(rounded_avg)[2:]  # Convert to binary and remove the '0b' prefix