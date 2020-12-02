matching_brackets = {
    ")": "(",
    "]": "[",
    "}": "{",
}


def is_paired(input_string):
    open_brackets = []

    for c in input_string:
        if c in matching_brackets.values():
            open_brackets.append(c)
        elif c in matching_brackets.keys():
            try:
                if matching_brackets[c] != open_brackets.pop():
                    return False
            except IndexError:
                return False

    return not open_brackets
