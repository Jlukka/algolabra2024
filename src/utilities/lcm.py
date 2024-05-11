"""Module that provides a function to calculate the least common multiple of two numbers
"""
from .gcd import greatestCommonDivisor


def least_common_multiple(a, b):
    """Function to calculate the least common multiple of two numbers

    Args:
        a (int): First number
        b (int): Second number

    Returns:
        int: Lowest common multiple of a and b
    """
    return abs(a * b) // greatestCommonDivisor(a, b)
