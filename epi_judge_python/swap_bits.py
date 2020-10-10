from test_framework import generic_test


def swap_bits(x, i, j):
    # get value of bits at positions a and b
    a_bit = x >> i & 1
    b_bit = x >> j & 1

    # set bit at position a to b_bit and visa versa
    x ^= (-a_bit ^ x) & (1 << j)
    x ^= (-b_bit ^ x) & (1 << i)
    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('swap_bits.py', 'swap_bits.tsv',
                                       swap_bits))
