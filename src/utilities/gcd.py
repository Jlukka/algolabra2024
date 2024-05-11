"""Module which provides an implementation of the
euclidean algorithm for finding the greatest
common divisor of two numbers
"""
def greatest_common_divisor(a, b):
    """Function that performs the euclidean
    algorithm on the provided numbers

    Args:
        a (int): First number
        b (int): Second number

    Returns:
        int: The greatest common divisor between
        the two numbers
    """
    while b != 0:
        b, a = a % b, b
    return a
