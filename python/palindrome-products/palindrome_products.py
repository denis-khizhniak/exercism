from collections import defaultdict


def cache_result(func):
    cache = dict()

    def wrap(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return wrap


@cache_result
def palindrom_products_factors(min_factor, max_factor):
    products = defaultdict(list)

    factors = [
        (i * j, (i, j))
        for i in range(min_factor, max_factor + 1)
        for j in range(i, max_factor + 1)
        if str(i * j)[::-1] == str(i * j)
    ]

    for k, v in factors:
        products[k].append(v)

    return products


def extreme(min_factor, max_factor, extreme_func):
    # validate range
    if max_factor < min_factor:
        raise ValueError("max range cannot be less than min range!")

    # set default min_factor if not set
    if min_factor is None:
        min_factor = 0

    products = palindrom_products_factors(min_factor, max_factor)

    if len(products) == 0:
        return (None, [])

    extreme_product = extreme_func(products)
    extreme_product_factors = products[extreme_product]

    return extreme_product, extreme_product_factors


def largest(min_factor, max_factor):
    return extreme(min_factor, max_factor, max)


def smallest(min_factor, max_factor):
    return extreme(min_factor, max_factor, min)
