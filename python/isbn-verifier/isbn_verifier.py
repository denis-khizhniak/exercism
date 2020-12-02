import re


def is_valid(isbn):
    if len(re.findall(r"\d|X", isbn)) != 10:
        return False

    return (
        sum(
            int(m.group(0).replace("X", "10")) * (10 - idx)
            for idx, m in enumerate(re.finditer(r"\d|X$", isbn))
        )
        % 11
        == 0
    )
