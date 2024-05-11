"""Module that provides a class that generates keys for
RSA encryption
"""
from .primegenerator import PrimeGenerator
from .lcm import least_common_multiple
from .gcd import greatestCommonDivisor
from .extended_gcd import multiplicative_inverse

class KeyGenerator:
    """Class that provides functions to generate RSA
    encryption keys
    """
    def __init__(self):
        """Class constructor that creates a new instance of KeyGenerator
        """
        self.bits = 1024
        self.prime_generator = PrimeGenerator()
        self.exponent = 65537

    def __check_too_close(self, p, q):
        """Checks if the two primes are too close to one another
        for security purposes

        Args:
            p (int): First prime
            q (int): Second prime

        Returns:
            bool: Boolean that states whether the primes are too close
            to one another to be usable for key making
        """
        return abs(p - q) <= 2**((self.bits // 2) - 100)

    def __check_lambda_n(self, lambda_n):
        """Function that checks if the exponent and lambda n are coprime

        Args:
            lambda_n (int): Totient of p and q

        Returns:
            bool: Boolean that states whether lambda n can be used for keymaking
            (the function returns true if lambda n and exponent are not coprime)
        """
        return greatestCommonDivisor(lambda_n, self.exponent) != 1

    def __check_if_key_can_be_made(self, p, q):
        """Function that performs necessary checks to ensure the keys
        can be created without issues

        Args:
            p (int): First prime
            q (int): Second prime

        Returns:
            bool: Boolean that states whether the keys can be created 
            from p and q
        """
        if self.__check_too_close(p, q):
            return (False, None)

        lambda_n = least_common_multiple(p - 1, q - 1)

        if self.__check_lambda_n(lambda_n):
            return (False, None)

        try:
            d = multiplicative_inverse(self.exponent, lambda_n)
        except ValueError:
            return (False, None)

        return (True, d)

    def generate_keys(self):
        """Function that runs until two valid primes are found
        and public and private encryption keys are created from
        the prime numbers

        Returns:
            tuple: Tuple where the contents are (public key, private key)
        """
        while True:
            p, q = self.__generate_two_primes()

            n = p * q

            success, d = self.__check_if_key_can_be_made(p, q)

            if success:
                pub_key = str(bin(n)[2:]) + str(bin(self.exponent)[2:])

                priv_key = str(bin(n)[2:]) + str(bin(d)[2:])

                return (pub_key, priv_key)

    def __generate_two_primes(self):
        """Auxiliary function that generates two probable prime
        numbers for the key generation function

        Returns:
            int: Tuple where contents are (first prime, second prime)
        """
        first_prime = self.prime_generator.generatePrime(self.bits)
        second_prime = self.prime_generator.generatePrime(self.bits)
        return (first_prime, second_prime)
