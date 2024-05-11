import unittest

from utilities.rsa import encrypt, decrypt
from utilities.keygen import KeyGenerator


class TestRSA(unittest.TestCase):
    def setUp(self):
        self.keyGenerator = KeyGenerator()
        self.pub_key, self.priv_key = self.keyGenerator.generate_keys()
        self.small_message = 65
        self.large_message = int("1234567890" * 30)

    def test_small_message_encryption_with_pub_key_works(self):
        self.assertNotEqual(
            encrypt(self.small_message, self.pub_key), self.small_message)

    def test_small_message_encryption_with_priv_key_works(self):
        self.assertNotEqual(
            encrypt(self.small_message, self.priv_key), self.small_message)

    def test_small_pub_encrypted_message_decryption_with_priv_key_works(self):
        pub_encrypted_message = encrypt(self.small_message, self.pub_key)
        self.assertEqual(decrypt(pub_encrypted_message,
                         self.priv_key), self.small_message)

    def test_small_priv_encrypted_message_decryption_with_pub_key_works(self):
        priv_encrypted_message = encrypt(self.small_message, self.priv_key)
        self.assertEqual(decrypt(priv_encrypted_message,
                         self.pub_key), self.small_message)

    def test_small_pub_encrypted_message_decryption_with_pub_key_doesnt_work(
            self):
        pub_encrypted_message = encrypt(self.small_message, self.pub_key)
        self.assertNotEqual(decrypt(pub_encrypted_message,
                            self.pub_key), self.small_message)

    def test_small_priv_encrypted_message_decryption_with_priv_key_doesnt_work(
            self):
        priv_encrypted_message = encrypt(self.small_message, self.priv_key)
        self.assertNotEqual(decrypt(priv_encrypted_message,
                            self.priv_key), self.small_message)

    def test_large_message_encryption_with_pub_key_works(self):
        self.assertNotEqual(
            encrypt(self.large_message, self.pub_key), self.large_message)

    def test_large_message_encryption_with_priv_key_works(self):
        self.assertNotEqual(
            encrypt(self.large_message, self.priv_key), self.large_message)

    def test_large_pub_encrypted_message_decryption_with_priv_key_works(self):
        pub_encrypted_message = encrypt(self.large_message, self.pub_key)
        self.assertEqual(decrypt(pub_encrypted_message,
                         self.priv_key), self.large_message)

    def test_large_priv_encrypted_message_decryption_with_pub_key_works(self):
        priv_encrypted_message = encrypt(self.large_message, self.priv_key)
        self.assertEqual(decrypt(priv_encrypted_message,
                         self.pub_key), self.large_message)

    def test_large_pub_encrypted_message_decryption_with_pub_key_doesnt_work(
            self):
        pub_encrypted_message = encrypt(self.large_message, self.pub_key)
        self.assertNotEqual(decrypt(pub_encrypted_message,
                            self.pub_key), self.large_message)

    def test_large_priv_encrypted_message_decryption_with_priv_key_doesnt_work(
            self):
        priv_encrypted_message = encrypt(self.large_message, self.priv_key)
        self.assertNotEqual(decrypt(priv_encrypted_message,
                            self.priv_key), self.large_message)
