import unittest

from utilities.keygen import KeyGenerator


class TestKeygen(unittest.TestCase):
    def setUp(self):
        self.keyGenerator = KeyGenerator()

    def test_key_generator_creates_two_keys_which_are_not_equal(self):
        public_key, private_key = self.keyGenerator.generate_keys()
        self.assertNotEqual(public_key, private_key)

    def test_private__check_too_close_functions_correctly_close_numbers(self):
        result = self.keyGenerator._KeyGenerator__check_too_close(2**1024, 2**1024 + 2**250)
        self.assertTrue(result)

    def test_private__check_too_close_functions_correctly_not_close_numbers(self):
        result = self.keyGenerator._KeyGenerator__check_too_close(1024, 2**1024 + 1**1023)
        self.assertFalse(result)

    def test_private__check_lambda_n_functions_correctly_coprimes(self):
        result = self.keyGenerator._KeyGenerator__check_lambda_n(2**1279 - 1)
        self.assertFalse(result)
        
    def test_private_check_lambda_n_functions_correctly_not_coprimes(self):
        result = self.keyGenerator._KeyGenerator__check_lambda_n((2**607 - 1) * 65537)
        self.assertTrue(result)