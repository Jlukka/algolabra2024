"""Module that provides a class to generate primes with
"""
from random import randint

from .sieve import Sieve
from .millerrabin import MillerRabin

class PrimeGenerator: # pylint: disable=too-few-public-methods
    """Class that provides a function used to generate probable primes with."""

    def __init__(self):
        """Class constructor that creates a new instance of the PrimeGenerator"""
        self.sieve = Sieve(2500)
        self.miller_rabin = MillerRabin(40)

    def generate_prime(self, bits):
        """Function that generates probable primes when called of wanted bit length

        Args:
            bits (int): Determines how long the generated probable prime number should be in bits

        Returns:
            int: Probable prime number of wanted bit length
        """
        while True:
            candidate = self.__generate_prime_candidate(bits)
            if self.__test_prime_candidate(candidate):
                return candidate

    def __test_prime_candidate(self, prime_candidate):
        """Private class that tests probable prime number candidates against Sieve of Eratosthenes
        and the Miller-Rabin primality test.

        Args:
            prime_candidate (int): Integer value being tested by the primality tests

        Returns:
            bool: Boolean that tells whether the candidate is a probable prime or not
        """
        if not self.sieve.primality_test(prime_candidate):
            return False
        if not self.miller_rabin.primality_test(prime_candidate):
            return False
        return True

    def __generate_prime_candidate(self, bits):
        """Function that generates random integers of wanted bit length

        Args:
            bits (int): Determines how long the integer should be in bit length

        Returns:
            int: A randomly chosen integer of wanted bit length
        """
        return randint(((2**(bits - 1)) + (2**(bits - 2) + 1)), (2**bits) - 1)
