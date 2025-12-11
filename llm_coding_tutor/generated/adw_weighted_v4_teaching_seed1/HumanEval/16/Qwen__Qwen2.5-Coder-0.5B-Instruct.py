import re
from typing import *
from collections import *

def count_distinct_characters(string: str) -> int:
    # Convert the string to lowercase to ensure case insensitivity
    string = string.lower()
    
    # Remove all non-alphanumeric characters using regex
    cleaned_string = re.sub(r'[^a-zA-Z0-9]', '', string)
    
    # Convert the cleaned string into a set to get unique characters
    distinct_chars = set(cleaned_string)
    
    # Return the number of distinct characters
    return len(distinct_chars)