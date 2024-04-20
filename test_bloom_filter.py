# test_bloom_filter.py
import unittest
from bloom_filter import BloomFilter
import random
import string

def generate_random_string(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

class TestBloomFilter(unittest.TestCase):
    def setUp(self):
        self.bf = BloomFilter(1000, 5)  # A larger Bloom filter for more rigorous testing

    def test_random_strings(self):
        # Test with 100 random strings
        random_strings = [generate_random_string(10) for _ in range(100)]
        for string in random_strings:
            self.bf.add(string)
            self.assertTrue(self.bf.check(string))
        # Check for false positives
        self.assertFalse(self.bf.check(generate_random_string(10)))

if __name__ == '__main__':
    unittest.main()
