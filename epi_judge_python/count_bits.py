from test_framework import generic_test


# Hamming weight: https://en.wikipedia.org/wiki/Hamming_weight
def count_bits(x: int) -> int:
    num_bits = 0

    while x:
        num_bits += 1
        x &= x - 1

    return num_bits


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('count_bits.py', 'count_bits.tsv',
                                       count_bits))
