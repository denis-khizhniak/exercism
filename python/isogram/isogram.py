from collections import Counter


def is_isogram(string):
    if len(string) == 0:
        return True

    str = string.replace(" ", "").replace("-", "").lower()
    return Counter(str).most_common(1)[0][1] == 1
