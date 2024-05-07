from .primegenerator import PrimeGenerator
from .lcm import leastCommonMultiple
from .gcd import greatestCommonDivisor
from .extended_gcd import multiplicative_inverse
from .modexp import power

from pathlib import Path

a = PrimeGenerator()
bits = 1024

p = a.generatePrime(bits)
q = a.generatePrime(bits)
n = p*q
tooClose = (abs(p-q)<= 2**((bits//2)-100))
lambdaN = leastCommonMultiple(p-1,q-1)



def generateKeys(bits, name):
    a = PrimeGenerator()

    exponent = 65537

    finished = False
    while not finished:
        p = a.generatePrime(bits)
        q = a.generatePrime(bits)

        if (abs(p-q)<= 2**((bits//2)-100)):
            continue

        lambdaN = leastCommonMultiple(p-1,q-1)
        if greatestCommonDivisor(lambdaN, exponent) != 1:
            continue

        n = p*q

        d = multiplicative_inverse(exponent, lambdaN)

        folder = Path("./keys").mkdir(exist_ok=True) or Path("./keys")

        pub_key = str(bin(n)[2:])+str(bin(exponent)[2:])

        priv_key = str(bin(n)[2:])+str(bin(d)[2:])

        pub_key_file = folder.joinpath(name + "_pub.txt")

        priv_key_file = folder.joinpath(name + "_priv.txt")

        pub_key_file.write_text(pub_key)

        priv_key_file.write_text(priv_key)

        finished = True

"""
        message = 19215303908453569823336757320931988257576159024438864032515723337657564869766754517224764645710830934557031676482438517004038561240340994336375309339180586249519911472398339791774312571680940680967659620614658306044009087750665828756328188910569534857453672811698669202405160539829074817814422384317244826589463150191151153397031848302579849657296483674856994783238797091824941371719456490421995007067863058656145609644950696231904617923919232189824477996008863296782030536688129339133750960391123559245690178118087707259619112222333887430269039755585740050266758895780336034799585843815131368293166113613778946347939
        print(f"message {message}")
        encrypted_message = power(message, exponent, n)
        print(f"encrypted message {encrypted_message}")
        decrypted_message = power(encrypted_message, d, n)
        print(f"decrypted_message {decrypted_message}")
        print(message == decrypted_message)
"""

if __name__ == "__main__":
    generateKeys(1024, "test")