"""Module that provides RSA encrypt and decrypt functions
"""
def encrypt(message, key):
    """Function that performs RSA encryption on a message with a given key

    Args:
        message (int): Message that gets encrypted
        key (int): Key that's used to encrypt the message with

    Returns:
        int: Returns message encrypted with key
    """
    n = int(key[:2048], 2)
    exponent = int(key[2048:], 2)
    return pow(message, exponent, n)


def decrypt(encrypted_message, key):
    """Function that performs RSA decryption on a message with a given key

    Args:
        encrypted_message (int): Encrypted message that gets decrypted
        key (int): Key that's used to decrypt the message with

    Returns:
        int: Returns encrypted_message decrypted with key
    """
    n = int(key[:2048], 2)
    d = int(key[2048:], 2)
    return pow(encrypted_message, d, n)
