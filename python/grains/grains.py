def square(number):
    if not 1 <= number <= 64:
        raise ValueError("Number must be in range 1..64")

    return 2 ** (number - 1)


def total():
    return sum(2 ** (i-1) for i in range(1, 65))
