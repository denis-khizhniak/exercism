import itertools


band_colors = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
]


def value(colors):
    number = int(
        "".join(
            (
                str(band_colors.index(col))
                for _, col in itertools.takewhile(lambda t: t[0] < 2, enumerate(colors))
            )
        )
    )

    return number
