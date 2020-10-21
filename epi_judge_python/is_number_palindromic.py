from test_framework import generic_test


def is_palindrome_number(x: int) -> bool:
    reverse, aux_x = 0, x

    if x < 0:
        return False

    while aux_x:
        reverse *= 10
        reverse += aux_x % 10
        aux_x //= 10

    return x == reverse


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_number_palindromic.py',
                                       'is_number_palindromic.tsv',
                                       is_palindrome_number))
