import re
from datetime import datetime

def valid_date(date):
    # Define the regular expression pattern for a valid date string
    date_pattern = r'^\d{2}-\d{2}-\d{4}$'
    
    # Check if the date matches the pattern
    if not re.match(date_pattern, date):
        return False
    
    # Split the date into month, day, and year components
    month, day, year = map(int, date.split('-'))
    
    # Define the months with their respective number of days
    months_with_days = {
        1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    
    # Validate the month and day numbers
    if month < 1 or month > 12:
        return False
    if day < 1 or day > months_with_days[month]:
        return False
    
    # Check if the year is valid
    try:
        datetime.strptime(year, '%Y')
    except ValueError:
        return False
    
    return True