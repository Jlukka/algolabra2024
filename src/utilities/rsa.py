from .modexp import power

def encrypt(message, key):
    n = int(key[:2048], 2)
    exponent = int(key[2048:],2)
    return power(message, exponent, n)


def decrypt(encrypted_message, key):
    n = int(key[:2048], 2)
    d = int(key[2048:],2)
    return power(encrypted_message, d, n)
