"""Module that provides extended euclidean algorithm to calculate
modular multiplicative inverses of two numbers
"""
def multiplicative_inverse(a, b):
    """Function that calculates the modular multiplicative inverse
    of two numbers

    Args:
        a (int): First number
        b (int): Second number

    Returns:
        int: Modular multiplicative inverse of a and b
    """
    old_t, new_t = 0, 1
    old_r, new_r = b, a

    while new_r != 0:
        quotient = old_r // new_r
        old_t, new_t = new_t, old_t - (quotient * new_t)
        old_r, new_r = new_r, old_r - (quotient * new_r)

    if old_r > 1:
        return None
    if old_t < 0:
        return old_t + b
    return old_t
