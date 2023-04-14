import unittest
from src.fizz_buzz import *

class TestFizzBuzz(unittest.TestCase):
    
    def test_fizz_outputted_when_3_entered(self):
        self.assertEqual("Fizz", fizz_buzz(3))
    # self.assertEqual(expected, actual)

    def test_buzz_outputted_when_5_entered(self):
        self.assertEqual("Buzz", fizz_buzz(5))
    
    def test_fizz_buzz_outputed_when_divisible_by_3_and_5(self):
        self.assertEqual("FizzBuzz", fizz_buzz(30))

    def test_number__converted_to_str(self):
        self.assertEqual("7", fizz_buzz(7))