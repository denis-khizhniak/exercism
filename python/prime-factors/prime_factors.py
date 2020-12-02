def factors(value):
    quotient = value
    prime_factors = []

    divisor = 2
    while divisor <= quotient:
        if quotient % divisor == 0:
            quotient = quotient / divisor
            prime_factors.append(divisor)
        else:
            divisor += 1

    return prime_factors
