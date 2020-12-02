import re


def remove_extra_characters(func):
    def wrap(string):
        cleaned_string = re.sub(r"[^A-Za-z!?]", "", string)
        return func(cleaned_string)

    return wrap


@remove_extra_characters
def has_all_capitals(string):
    return string.upper() == string and re.match(r"[A-Z]+", string) is not None


@remove_extra_characters
def is_question(string):
    if not string:
        return False

    return string[-1] == "?"


def response(hey_bob):
    RESPONSE_YELLED = "Whoa, chill out!"
    RESPONSE_QUESTION = "Sure."
    RESPONSE_YELLED_QUESTION = "Calm down, I know what I'm doing!"
    RESPONSE_EMPTY = "Fine. Be that way!"
    RESPONSE_GENERAL = "Whatever."

    if re.match(r"\s*$", hey_bob):
        return RESPONSE_EMPTY
    elif has_all_capitals(hey_bob) and is_question(hey_bob):
        return RESPONSE_YELLED_QUESTION
    elif has_all_capitals(hey_bob):
        return RESPONSE_YELLED
    elif is_question(hey_bob):
        return RESPONSE_QUESTION
    else:
        return RESPONSE_GENERAL
