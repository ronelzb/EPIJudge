from test_framework import generic_test


def reverse(x: int) -> int:
    result, abs_x = 0, abs(x)

    while abs_x:
        result *= 10
        result += abs_x % 10  # get most significant digit
        abs_x //= 10  # remove least significant digit

    return -result if x < 0 else result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
