import unittest
import num2words
from Challenges.fibonacci import *


class Challenge4(unittest.TestCase):

    def test_challenge4(self):
        print(str(fibonacci(21)) + ": " + num2words.num2words(fibonacci(21)))
    if __name__ == '__main__':
        unittest.main()
