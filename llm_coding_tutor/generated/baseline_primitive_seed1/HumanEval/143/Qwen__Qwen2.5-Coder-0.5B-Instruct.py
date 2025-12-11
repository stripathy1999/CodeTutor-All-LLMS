from collections import defaultdict

def words_in_sentence(sentence):
    prime_lengths = defaultdict(int)
    for word in sentence.split():
        for i, char in enumerate(word):
            if int(char) in prime_lengths:
                prime_lengths[int(char)] += 1
            else:
                prime_lengths[int(char)] = 1
    # Find all words with prime length
    prime_length_words = [word for word in sentence.split() if prime_lengths[word] == len(prime_lengths)]
    # Sort the words by their length
    prime_length_words.sort(key=len)
    # Join the sorted words with spaces
    result =''.join(prime_length_words)
    return result

# Test cases
print(words_in_sentence("This is a test"))  # Output: "is"
print(words_in_sentence("lets go for swimming"))  # Output: "go for"
```