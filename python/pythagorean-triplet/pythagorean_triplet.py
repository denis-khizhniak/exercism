def triplets_with_sum(number):
    triplets = []

    for a in range(1, number // 3):
        for b in range(a + 1, (number - a) // 2 + 1):
            c = number - a - b
            if is_triplet([a, b, c]):
                triplets.append([a, b, c])

    return triplets


def triplets_in_range(start, end):
    triplets = []

    for n in range(start, end + 1):
        triplets.extend(triplets_with_sum(n))

    return triplets


def is_triplet(triplet):
    has_three_elements = len(triplet) == 3

    a, b, c = triplet
    inequality_is_correct = a < b < c

    equation_is_correct = a ** 2 + b ** 2 == c ** 2

    return all([has_three_elements, inequality_is_correct, equation_is_correct])
