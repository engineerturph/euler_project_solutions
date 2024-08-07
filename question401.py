import math

modulo_number = 10 ** 9
def sum_of_squares(n):
    """
    Calculate the sum of squares of the first n natural numbers using the formula.

    Parameters:
    n (int): The number up to which the squares are to be summed.

    Returns:
    int: The sum of the squares of the first n natural numbers.
    """
    return (n * (n + 1) * (2 * n + 1) // 6) % modulo_number


def sigma_function(n):
    root_n = int(n ** 0.5)
    root_up = root_n + 1
    squares = [(i * i) for i in range(1, root_n + 1)]
    result = 0
    harmonic_series = [n // i for i in range(1,root_up+1)]
    for i in range(1, root_n + 1):
        result+= squares[i-1] * (n // i)
        result = result % modulo_number
    for i in range(root_up -1):
        how_much = i + 1
        result += how_much * (sum_of_squares(harmonic_series[i]) - sum_of_squares(harmonic_series[i+1]))
        result = result % modulo_number
    return result

print(sigma_function(10**15))
