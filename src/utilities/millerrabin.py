"""Module that provides an implementation of the miller rabin primality test
"""
from random import randint

class MillerRabin(): # pylint: disable=too-few-public-methods
    """Class that provides an implementation of the miller rabin primality test
    """
    def __init__(self, attempts):
        """Class constructor that creates a new instance of the MillerRabin class

        Args:
            attempts (int): How many times the miller rabin test is run on the number
            before it has considered pasing the primality test (and is a probable prime)
        """
        self.attempts = attempts

    def primality_test(self, number):
        """Function that tests a number against the miller rabin primality test
        a specified number of times

        Args:
            number (int): How many times should the program attempt the miller-rabin
            primality test before a number is considered a probable prime

        Returns:
            bool: A boolean that states whether a number is a probable prime or not
        """
        if number == 1:
            return False

        if number % 2 == 0:
            return False

        for _ in range(0, self.attempts):
            if not self.__miller_rabin(number):
                return False
        return True

    def __miller_rabin(self, number):
        """Private auxiliary function that performs one iteration of the miller rabin
        primality test

        Args:
            number (int): A prime candidate to be run through the primality test

        Returns:
            bool: Whether the candidate is a probable prime or not
        """
        a = randint(2, number - 2)

        d, s = self.__find_d_and_s(number)

        x = pow(a, d, number)
        for _ in range(0, s):
            y = pow(x, 2, number)

            if y == 1 and x != 1 and x != number - 1:
                return False

            x = y
        if y != 1:
            return False
        return True

    def __find_d_and_s(self, number):
        """Private auxiliary function used to find d and s which are
        values used by one iteration of the miller-rabin primality
        test

        Args:
            number (int): A prime candidate

        Returns:
            tuple: Tuple which is constructed as (d, s)
        """
        d = number - 1
        s = 0
        while d % 2 == 0:
            d //= 2
            s += 1
        return d, s
