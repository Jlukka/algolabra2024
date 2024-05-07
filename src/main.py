from utilities.keygen import generateKeys
from utilities.rsa import encrypt, decrypt

from random import randint
from pathlib import Path

def create_keys_with_name(name):
    generateKeys(1024, name)

def encrypt_with_key_name(message, pub_key):
    return encrypt(message, pub_key)

def decrypt_with_key_name(message, priv_key):
    return decrypt(message, priv_key)


while True:
    print("1. create new keys")
    print("2. encrypt a message")
    print("3. decrypt a message")
    print("4. generate random message")
    print("5. list keys ")
    print("x. exit")

    action = input("enter number of action you wish to perform ")
    if action == "1":
        name = input("name the keys ")
        pub_key_found = Path("./keys") / (name + "_pub.txt")
        priv_key_found = Path("./keys") / (name + "_priv.txt")
        if pub_key_found.is_file() or priv_key_found.is_file():
            print("keys already exist")
            continue
        else:
            create_keys_with_name(name)
            print(f"keys created called {name}_pub.txt {name}_priv.txt")

    if action == "2":
        message = input("enter the message you want to encrypt (integer) ")
        try:
            message = int(message)
        except:
            print("not a valid integer")
            continue

        name = input("name of the key to use for the encryption (e.g. test_pub or test_priv) ")

        pub_key_found = Path("./keys") / (name + ".txt")

        if not pub_key_found.is_file():
            print("not a valid key name")
            continue
        else:
            with pub_key_found.open(mode="r") as pub_key_file:
                pub_key = pub_key_file.read()

                print(f"encrypted message: \n {encrypt_with_key_name(message, pub_key)}")


    if action == "3":
        message = input("enter the message you want to decrypt (integer) ")
        try:
            message = int(message)
        except:
            print("not a valid integer")
            continue

        name = input("name of the key to use for the decryption ")

        priv_key_found = Path("./keys") / (name + ".txt")

        if not priv_key_found.is_file():
            print("not a valid key name")
            continue
        else:
            with priv_key_found.open(mode="r") as priv_key_file:
                priv_key = priv_key_file.read()

                print(f"encrypted message: \n {decrypt_with_key_name(message, priv_key)}")

    if action == "4":
        bits = input("enter how many bits long the data should be (only values shorter than 2048 work) ")
        try:
            bits = int(bits)
            message = randint(2**(bits-1)+1, 2**bits)
            print(message)
        except:
            print("not a valid integer")
            continue

    if action == "5":
        keys = Path("./keys")
        [print(key.stem) for key in keys.iterdir() if key.is_file()]

    if action == "x":
        break
"""
    generateKeys(1024, name)

    pub_key_path = Path("./keys") / (name + "_pub.txt")

    priv_key_path = Path("./keys") / (name + "_priv.txt")


    with pub_key_path.open(mode="r") as pub_key_file:
        pub_key = pub_key_file.read()

    with priv_key_path.open(mode="r") as priv_key_file:
        priv_key = priv_key_file.read()

    encrypted_message = encrypt(message, pub_key)

    print(encrypted_message)

    decrypted_message = decrypt(encrypted_message, priv_key)

    print(decrypted_message)

    print(decrypted_message==message)

    break
"""