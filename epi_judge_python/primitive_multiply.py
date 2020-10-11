from test_framework import generic_test


def multiply(x: int, y: int) -> int:
    is_negative = False

    if x < 0 and y < 0:
        x = -x
        y = -y
    elif x < 0:
        x = -x
        is_negative = True
    elif y < 0:
        y = -y
        is_negative = True

    result = 0

    # multiply(x, y) = | multiply(x*2, y/2) if y is even
    #                  | y + multiply(x*2, y/2) if y is odd
    while y:
        if y & 1:
            result += x
        x <<= 1  # multiply by 2
        y >>= 1  # divide by 2

    return -result if is_negative else result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_multiply.py',
                                       'primitive_multiply.tsv', multiply))
