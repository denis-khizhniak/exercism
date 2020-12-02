def classify(number):
    if sum(generate_factors(number)) == number:
        return "perfect"
    elif sum(generate_factors(number)) > number:
        return "abundant"
    else:
        return "deficient"


def generate_factors(number):
    if number <= 0:
        raise ValueError(f"Cannot calculate factors of the number \"{number}\"!")
    else:
        return (i for i in range(1, number) if number % i == 0)
