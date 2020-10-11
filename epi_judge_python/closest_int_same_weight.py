from test_framework import generic_test


def closest_int_same_bit_count(x: int) -> int:
    first_zero = ~x & (x + 1)
    first_one = x & ~(x - 1)
    if first_zero > first_one:
        x |= first_zero
        x ^= first_zero >> 1
    else:
        x ^= first_one
        x |= first_one >> 1

    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('closest_int_same_weight.py',
                                       'closest_int_same_weight.tsv',
                                       closest_int_same_bit_count))
