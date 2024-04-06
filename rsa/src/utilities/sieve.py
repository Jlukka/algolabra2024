import math

class Sieve():
    def __init__(self, n):
        self.primes = self.primesUnderN(n)


    def primesUnderN(self, n):
        primeList = list(range(2,n))
        i = 2
        while i < math.sqrt(n):
            j = 2
            while i*j <= n:
                try:
                    primeList.remove(i*j)
                except:
                    pass
                j += 1
            i += 1
        return primeList
    
    def primalityTest(self, number):
        for prime in self.primes:
            if number % prime == 0:
                return False
        return True
    


a = Sieve(2500)
print(a.primalityTest(19134702400093278081449423917))