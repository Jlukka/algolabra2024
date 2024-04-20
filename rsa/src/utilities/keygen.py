from primegenerator import PrimeGenerator
from lcm import leastCommonMultiple
from gcd import greatestCommonDivisor
from extended_gcd import multiplicative_inverse
from modexp import power

a = PrimeGenerator()
bits = 1024

p = a.generatePrime(bits)
q = a.generatePrime(bits)
n = p*q
tooClose = (abs(p-q)<= 2**((bits//2)-100))
lambdaN = leastCommonMultiple(p-1,q-1)



def generateKeys(bits):
    a = PrimeGenerator()

    finished = False
    while not finished:
        p = a.generatePrime(bits)
        q = a.generatePrime(bits)

        if (abs(p-q)<= 2**((bits//2)-100)):
            continue

        lambdaN = leastCommonMultiple(p-1,q-1)
        if greatestCommonDivisor(lambdaN, 65537) != 1:
            continue

        n = p*q

        d = multiplicative_inverse(65537, lambdaN)

        print (f"n    {n}")
        print (f"d    {d}")

        message = 1337
        print(f"message {message}")
        encrypted_message = power(message, 65537, n)
        print(f"encrypted message {encrypted_message}")
        decrypted_message = power(encrypted_message, d, n)
        print(f"decrypted_message {decrypted_message}")
        finished = True


if __name__ == "__main__":
    generateKeys(1024)