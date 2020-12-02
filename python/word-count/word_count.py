from collections import Counter
import re


def count_words(sentence):
    words = re.findall(r"[A-Za-z0-9']+|", sentence.lower())

    # clean words from surrounding quotes
    words = [w.strip("'\"") for w in words]

    return dict(Counter(filter(None, words)))
