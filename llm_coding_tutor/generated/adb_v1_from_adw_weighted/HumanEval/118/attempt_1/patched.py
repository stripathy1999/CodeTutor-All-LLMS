def get_closest_vowel(word):
    """You are given a word. Your task is to find the closest vowel that stands between 
    two consonants from the right side of the word (case sensitive).
    
    Vowels in the beginning and ending doesn't count. Return empty string if you didn't
    find any vowel met the above condition. 

    You may assume that the given string contains English letter only.

    Example:
    get_closest_vowel("yogurt") ==> "u"
    get_closest_vowel("FULL") ==> "U"
    get_closest_vowel("quick") ==> ""
    get_closest_vowel("ab") ==> ""
    """
    # Check for edge cases
    if not word:
        return ""
    if len(word) == 1:
        return ""
    if word[0].islower() and word[-1].islower():
        return ""

    # Find the closest vowel
    closest_vowel = ""
    for i in range(len(word) - 2):
        if word[i].isalpha() and word[i + 1].isalpha() and word[i + 2].isalpha():
            closest_vowel = word[i + 1]
            break

    return closest_vowel