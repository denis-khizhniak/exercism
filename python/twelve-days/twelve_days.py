numbers = {
    1: ["a", "first"],
    2: ["two", "second"],
    3: ["three", "third"],
    4: ["four", "fourth"],
    5: ["five", "fifth"],
    6: ["six", "sixth"],
    7: ["seven", "seventh"],
    8: ["eight", "eighth"],
    9: ["nine", "ninth"],
    10: ["ten", "tenth"],
    11: ["eleven", "eleventh"],
    12: ["twelve", "twelfth"],
}

day_gifts = {
    1: "Partridge in a Pear Tree",
    2: "Turtle Doves",
    3: "French Hens",
    4: "Calling Birds",
    5: "Gold Rings",
    6: "Geese-a-Laying",
    7: "Swans-a-Swimming",
    8: "Maids-a-Milking",
    9: "Ladies Dancing",
    10: "Lords-a-Leaping",
    11: "Pipers Piping",
    12: "Drummers Drumming",
}


def recite_verse(verse):
    verse_lines = []

    # initial line
    verse_lines.append(
        f"On the {numbers[verse][1]} day of Christmas my true love gave to me: "
    )

    # compose main lines
    verse_lines.extend(
        [f"{numbers[i][0]} {day_gifts[i]}" for i in reversed(range(1, verse + 1))]
    )

    # get middle lines comma separated
    verse_middle = ", ".join(verse_lines[1:-1])

    # complete the last line
    if verse > 1:
        verse_lines[verse] = ", and " + verse_lines[verse]
    verse_lines[verse] += "."

    return "".join((verse_lines[0], verse_middle, verse_lines[verse]))


def recite(start_verse, end_verse):
    return [recite_verse(n) for n in range(start_verse, end_verse + 1)]
