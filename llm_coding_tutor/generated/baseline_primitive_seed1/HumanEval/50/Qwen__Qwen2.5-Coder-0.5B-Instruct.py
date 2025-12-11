from collections import Counter

def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    """
    count = Counter(s)
    decoded = []
    for ch, freq in count.items():
        decoded.append(chr(((ord(ch) - 5 + ord("a")) % 26) + ord("a")))
    return "".join(decoded)

# test
print(decode_shift(encode_shift("abcde")) == "efghij")
print(decode_shift(encode_shift("hello world")) == "lipps asvph")
print(decode_shift(encode_shift("python programming")) == "uifqyqmpvph")<|end>