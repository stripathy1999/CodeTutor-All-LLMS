return number % 1

# check the correctness of the function
assert truncate_number(3.5) == 0.5
assert truncate_number(9.9999) == 0.9999
assert truncate_number(0.123456789) == 0.123456789
assert truncate_number(1000.0) == 0
assert truncate_number(123.4567890123456789) == 0.4567890123456789
```