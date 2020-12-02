def steps(number):
    if number <= 0:
        raise ValueError("Cannot concert values less or equal to 0!")

    i = 0
    while number > 1:
        if number % 2 == 0:
            number /= 2
        else:
            number = 3 * number + 1
        i += 1

    return i
