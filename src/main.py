"""Module that runs the user interface for the
RSA encryption algorithm
"""
# pylint: disable-all
from random import randint
from pathlib import Path

from utilities.keygen import KeyGenerator
from utilities.rsa import encrypt, decrypt

def create_keys_with_name(filename):
    """Function that creates files storing the keys for a provided 
    filename, in format {name}_priv.txt and {name}_pub.txt
    Args:
        filename (str): What they keys will be called
    
    """
    key_generator = KeyGenerator()
    pub_key, priv_key = key_generator.generate_keys()
    folder = Path("./keys").mkdir(exist_ok=True) or Path("./keys")

    pub_key_file = folder.joinpath(filename + "_pub.txt")

    priv_key_file = folder.joinpath(filename + "_priv.txt")

    pub_key_file.write_text(pub_key)

    priv_key_file.write_text(priv_key)


def encrypt_with_key_name(message, encryption_key):
    """Encrypts a message with a given key

    Args:
        message (int): An integer that serves as the message
        for the RSA encryption algorithm
        encryption_key (str): The key to use for encrypting the message

    Returns:
        _type_: _description_
    """
    return encrypt(message, encryption_key)


def decrypt_with_key_name(message, decryption_key):
    """Decrypts a message with a given key

    Args:
        message (int): An integer that serves as the message
        for the RSA decryption algorithm
        decryption_key (str): The key to use for decrypting the message

    Returns:
        _type_: _description_
    """
    return decrypt(message, decryption_key)


while True:
    print("1. create new keys")
    print("2. encrypt a message")
    print("3. decrypt a message")
    print("4. generate random message")
    print("5. list keys ")
    print("x. exit\n")

    action = input("enter number of action you wish to perform ")
    if action == "1":
        name = input("\nname the keys ")
        pub_key_found = Path("./keys") / (name + "_pub.txt")
        priv_key_found = Path("./keys") / (name + "_priv.txt")
        if pub_key_found.is_file() or priv_key_found.is_file():
            print("\nkeys already exist")
            continue
        create_keys_with_name(name)
        print(f"\nkeys created called {name}_pub.txt {name}_priv.txt")

    if action == "2":
        message = input("\nenter the message you want to encrypt (integer) ")
        try:
            message = int(message)
        except ValueError:
            print("\nnot a valid integer")
            continue

        name = input(
            "name of the key to use for the encryption (e.g. test_pub or test_priv) ")

        public_key_found = Path("./keys") / (name + ".txt")

        if not public_key_found.is_file():
            print("\nnot a valid key name")
            continue
        with public_key_found.open(mode="r") as pub_key_file:
            public_key = pub_key_file.read()

            print(
                f"encrypted message: \n {encrypt_with_key_name(message, public_key)}")

    if action == "3":
        message = input("\nenter the message you want to decrypt (integer) ")
        try:
            message = int(message)
        except ValueError:
            print("\nnot a valid integer")
            continue

        name = input("\nname of the key to use for the decryption ")

        priv_key_found = Path("./keys") / (name + ".txt")

        if not priv_key_found.is_file():
            print("\nnot a valid key name")
            continue

        with priv_key_found.open(mode="r") as priv_key_file:
            priv_key = priv_key_file.read()

            print(
                f"\nencrypted message: \n {decrypt_with_key_name(message, priv_key)}")

    if action == "4":
        bits = input(
            "\nenter how many bits long the data should be (only values shorter than 2048 work) ")
        try:
            bits = int(bits)
            message = randint(2**(bits - 1) + 1, 2**bits)
            print(message)
        except ValueError:
            print("\nnot a valid integer")
            continue

    if action == "5":
        keys = Path("./keys")
        [print(key.stem) for key in keys.iterdir() if key.is_file()]

    if action == "x":
        break
