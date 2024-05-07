from .sieve import Sieve
from .millerrabin import MillerRabin

from random import randint

class PrimeGenerator:
    def __init__(self):
        self.sieve = Sieve(10000)
        self.millerRabin = MillerRabin(40)

    def generatePrime(self, bits):
        isPrime = False

        while not isPrime:
            number = randint(((2**(bits-1))+(2**(bits-2)+1)), (2**bits) -1)
            if not self.sieve.primalityTest(number):
                continue
            if not self.millerRabin.primalityTest(number):
                continue
            break
        return number