from test_framework import generic_test


def power(x: float, y: int) -> float:
    result, y_power = 1.0, y

    if y < 0:
        y_power, x = -y_power, 1 / x

    while y_power:
        if y_power & 1:
            result *= x
        x *= x  # x to the power of 2       |
        y_power >>= 1  # divide power by 2  | (x^y/2)^2

    return result


if __name__ == '__main__':
    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv',
                                        power))
