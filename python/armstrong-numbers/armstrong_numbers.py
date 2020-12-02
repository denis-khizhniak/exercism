def is_armstrong_number(number):
    number_str = str(number)
    number_len = len(number_str)
    is_armstrong = False

    result = 0
    for d in number_str:
        result += pow(int(d), number_len)

    if float(number) == result:
        is_armstrong = True

    return is_armstrong
