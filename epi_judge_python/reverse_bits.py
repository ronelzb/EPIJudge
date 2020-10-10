from test_framework import generic_test


def reverse_bits(x: int) -> int:
    # '{:064b}' convert x into a 64 bit array
    b = '{:0{width}b}'.format(x, width=64)

    # reverse using built-in python and convert back to int
    return int(b[::-1], 2)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
