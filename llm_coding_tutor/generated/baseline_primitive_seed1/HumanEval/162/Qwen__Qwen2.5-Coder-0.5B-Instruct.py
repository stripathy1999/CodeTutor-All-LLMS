def string_to_md5(text):
    import hashlib
    if not text:
        return None
    md5_hash = hashlib.md5(text.encode()).hexdigest()
    return md5_hash

# Check function to verify the correctness of the solution
def check_solution():
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62', "Test case 1 failed"
    assert string_to_md5('') == None, "Test case 2 failed"
    assert string_to_md5('Python programming') == '3e25960a79dbc69b674cd4ec67a72c62', "Test case 3 failed"
    assert string_to_md5('Hashing MD5') == 'b32414714d89f38b926e380975f555f4', "Test case 4 failed"
    print("All test cases passed!")

check_solution()
```