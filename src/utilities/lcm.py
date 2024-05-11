"""Module that provides a function to calculate the least common multiple of two numbers
"""
from .gcd import greatest_common_divisor


def least_common_multiple(a, b):
    """Function to calculate the least common multiple of two numbers

    Args:
        a (int): First number
        b (int): Second number

    Returns:
        int: Lowest common multiple of a and b
    """
    return abs(a * b) // greatest_common_divisor(a, b)
