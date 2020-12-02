from itertools import permutations, combinations


def check_triangle(func):
    cache = dict()

    def wrap(sides):
        sides_hash = tuple(sides)
        if sides_hash in cache:
            return cache[sides_hash]

        if any(side <= 0 for side in sides):
            return False
            cache[sides_hash] = False

        perm = permutations(sides)

        if any(check[0] + check[1] < check[2] for check in perm):
            return False
            cache[sides_hash] = False

        return func(sides)

    return wrap


@check_triangle
def equilateral(sides):
    return sides[0] == sides[1] == sides[2]


@check_triangle
def isosceles(sides):
    comb = combinations(sides, 2)
    return any(check[0] == check[1] for check in comb)


@check_triangle
def scalene(sides):
    if not isosceles(sides) and not equilateral(sides):
        return True
    else:
        return False
