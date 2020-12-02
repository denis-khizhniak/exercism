def char_range(c1, c2):
    """Generates the characters from 'c1' to 'c2', inclusive."""
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)


def is_pangram(sentence):
    ENG_ALPHABET_CHARS_LEN = 26

    letters_set = set(l.lower() for l in sentence if l.lower() in char_range('a', 'z'))

    print(letters_set)

    return len(letters_set) == ENG_ALPHABET_CHARS_LEN
