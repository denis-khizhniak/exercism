import re


YACHT = 10
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 11
FOUR_OF_A_KIND = 12
LITTLE_STRAIGHT = 13
BIG_STRAIGHT = 14
CHOICE = 15


def check_rules_requirements(dice, category):
    requirements_rules = {
        YACHT: r"(\d)\1{4}",
        ONES: r"1+",
        TWOS: r"2+",
        THREES: r"3+",
        FOURS: r"4+",
        FIVES: r"5+",
        SIXES: r"6+",
        FULL_HOUSE: r"(\d)\1{2}(?!\1)(\d)\2|(\d)\3(?!\3)(\d)\4{2}",
        FOUR_OF_A_KIND: r"(\d)\1{3}(?!\1)",
        LITTLE_STRAIGHT: r"12345",
        BIG_STRAIGHT: r"23456",
        CHOICE: r"\d+",
    }

    return re.search(requirements_rules[category], "".join(map(str, sorted(dice))))


def score(dice, category):
    requirements_satisfied = check_rules_requirements(dice, category)

    if not requirements_satisfied:
        return 0

    calculated_scores = sum(int(char) for char in requirements_satisfied.group())
    scores = {
        YACHT: 50,
        ONES: calculated_scores,
        TWOS: calculated_scores,
        THREES: calculated_scores,
        FOURS: calculated_scores,
        FIVES: calculated_scores,
        SIXES: calculated_scores,
        FULL_HOUSE: calculated_scores,
        FOUR_OF_A_KIND: calculated_scores,
        LITTLE_STRAIGHT: 30,
        BIG_STRAIGHT: 30,
        CHOICE: calculated_scores,
    }

    return scores[category]
