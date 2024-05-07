from .gcd import greatestCommonDivisor

def leastCommonMultiple(a,b):
    return abs(a*b) // greatestCommonDivisor(a,b)