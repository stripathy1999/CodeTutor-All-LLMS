from collections import Counter

def find_max(words):
    return max([word for word in words if len(Counter(word)) == len(set(word))])

# check function to verify the correctness of the solution
def check_solution():
    assert find_max(["name", "of", "string"]) == "string", "Test case 1 failed"
    assert find_max(["name", "enam", "game"]) == "enam", "Test case 2 failed"
    assert find_max(["aaaaaaa", "bb","cc"]) == "", "Test case 3 failed"
    print("All test cases passed!")

check_solution()
```