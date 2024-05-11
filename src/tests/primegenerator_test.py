import unittest
from nprime import miller_rabin

from utilities.primegenerator import PrimeGenerator


class TestPrimeGenerator(unittest.TestCase):
    def setUp(self):
        self.primeGenerator = PrimeGenerator()

    def test_prime_generator_result_is_correct_length_small_number(self):
        bits = 100
        number = self.primeGenerator.generate_prime(bits)
        self.assertEqual(number.bit_length(), bits)

    def test_prime_generator_result_is_correct_length_moderate_number(self):
        bits = 500
        number = self.primeGenerator.generate_prime(bits)
        self.assertEqual(number.bit_length(), bits)

    def test_prime_generator_result_is_correct_length_realistic_number(self):
        bits = 1024
        number = self.primeGenerator.generate_prime(bits)
        self.assertEqual(number.bit_length(), bits)

    def test_prime_generator_result_passes_third_party_miller_rabin_small_number(
            self):
        bits = 100
        number = self.primeGenerator.generate_prime(bits)
        self.assertTrue(miller_rabin(number))

    def test_prime_generator_result_passes_third_party_miller_rabin_small_number(
            self):
        bits = 500
        number = self.primeGenerator.generate_prime(bits)
        self.assertTrue(miller_rabin(number))

    def test_prime_generator_result_passes_third_party_miller_rabin_small_number(
            self):
        bits = 1024
        number = self.primeGenerator.generate_prime(bits)
        self.assertTrue(miller_rabin(number))