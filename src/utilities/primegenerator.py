from .sieve import Sieve
from .millerrabin import MillerRabin

from random import randint

class PrimeGenerator:
    """Class that provides a function used to generate probable primes with."""

    def __init__(self):
        """Class constructor that creates a new instance of the PrimeGenerator"""
        self.sieve = Sieve(2500)
        self.millerRabin = MillerRabin(40)

    def generatePrime(self, bits):
        """Function that generates probable primes when called of wanted bit length

        Args:
            bits (int): Determines how long the generated probable prime number should be in bits

        Returns:
            int: Probable prime number of wanted bit length
        """
        while True:
            candidate = self.__generatePrimeCandidate(bits)
            if self.__testPrimeCandidate(candidate):
                return candidate
            else:
                continue

    def __testPrimeCandidate(self, primeCandidate):
        """Private class that tests probable prime number candidates against Sieve of Eratosthenes
        and the Miller-Rabin primality test.

        Args:
            primeCandidate (int): Integer value being tested by the primality tests

        Returns:
            bool: Boolean that tells whether the candidate is a probable prime or not
        """
        if not self.sieve.primality_test(primeCandidate):
            return False
        if not self.millerRabin.primalityTest(primeCandidate):
            return False
        return True

    def __generatePrimeCandidate(self, bits):
        """Function that generates random integers of wanted bit length

        Args:
            bits (int): Determines how long the integer should be in bit length

        Returns:
            int: A randomly chosen integer of wanted bit length
        """
        return randint(((2**(bits - 1)) + (2**(bits - 2) + 1)), (2**bits) - 1)
