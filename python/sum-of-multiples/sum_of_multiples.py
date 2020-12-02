def is_multiple_of(n, multiples):
    return any(n % m == 0 for m in multiples if m > 0)


def sum_of_multiples(limit, multiples):
    return sum(n for n in range(limit) if is_multiple_of(n, multiples))
