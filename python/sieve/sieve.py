from math import sqrt, floor


def primes(limit):
    primes_flags = [False] * 2 + [True] * (limit - 1)

    for i in range(2, floor(sqrt(limit))+1):
        for j in range(i ** 2, limit + 1, i):
            primes_flags[j] = False

    return [i for i, is_prime in enumerate(primes_flags) if is_prime]
