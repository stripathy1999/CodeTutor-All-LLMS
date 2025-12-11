def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if not text:
        return None
    return hashlib.md5(text.encode()).hexdigest()

# [INTENTIONAL_ERROR]: Rename the function to something else (different name).
# (Deliberate stress test for ADW robustness)

Output format:
- Return ONLY Python source code.
- No markdown, backticks, or explanations.
### Adaptive Weighted Rubric (Mode=teaching, mean_w=0.56)
- Preserve exact function name, parameters, and return type. (dim=correctness