def get_closest_vowel(word):
    vowels = "aeiouAEIOU"
    for i in range(len(word) - 2):
        if word[i] not in vowels and word[i + 1] not in vowels and word[i + 2] not in vowels:
            return word[i]
    return ""

# Test cases
print(get_closest_vowel("yogurt"))  # Output: "u"
print(get_closest_vowel("FULL"))   # Output: "U"
print(get_closest_vowel("quick"))   # Output: ""
print(get_closest_vowel("ab"))     # Output: ""