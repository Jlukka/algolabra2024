import unittest

from utilities.millerrabin import MillerRabin


class TestMillerRabin(unittest.TestCase):
    def setUp(self):
        self.millerRabin = MillerRabin(40)

    def test_miller_rabin_fails_if_given_one(self):
        self.assertFalse(self.millerRabin.primalityTest(1))

    def test_miller_rabin_fails_if_given_even_number(self):
        self.assertFalse(self.millerRabin.primalityTest(1024))

    def test_miller_rabin_succeeds_if_given_known_small_prime(self):
        self.assertTrue(self.millerRabin.primalityTest(719))

    def test_miller_rabin_succeeds_if_given_known_large_prime(self):
        self.assertTrue(self.millerRabin.primalityTest((2**1279) - 1))

    def test_miller_rabin_fails_if_given_moderately_sized_composite_number(
            self):
        self.assertFalse(self.millerRabin.primalityTest(
            8683317618811886495518194401279999999**2))

    def test_miller_rabin_fails_if_given_large_sized_composite_number(self):
        self.assertFalse(self.millerRabin.primalityTest(
            ((2**1279) - 1 * ((2**607) - 1))))
        
    def test_private__find_d_and_s_functions_correctly_small_number(self):
        expected = (55, 2)
        result = self.millerRabin._MillerRabin__findDandS(221)
        self.assertEqual(result, expected)

    def test_private__find_d_and_s_functions_correctly_moderate_number(self):
        expected = (2991309, 5)
        result = self.millerRabin._MillerRabin__findDandS(95721889)
        self.assertEqual(result, expected)