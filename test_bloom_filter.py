# test_bloom_filter.py
import unittest
from bloom_filter import BloomFilter
import random
import string

def generate_random_string(length):
    """ Generate a random string of given length. """
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))


def generate_dna_sequence(length):
    """ Generate a random DNA sequence of given length. """
    return ''.join(random.choice('ACGT') for _ in range(length))

class TestBloomFilter(unittest.TestCase):
    def setUp(self):
        self.bf = BloomFilter(1000, 5)

    def test_add_and_check(self):
        """ Test adding items and checking their existence. """
        item = "test_item"
        self.assertFalse(self.bf.check(item), "Item should not be present initially.")
        self.bf.add(item)
        self.assertTrue(self.bf.check(item), "Item should be present after being added.")
        
    def test_random_strings(self):
        """ Test Bloom filter with 100 random strings. """
        random_strings = [generate_random_string(10) for _ in range(100)]
        for string in random_strings:
            self.bf.add(string)
            self.assertTrue(self.bf.check(string))
        self.assertFalse(self.bf.check(generate_random_string(10)))

    def test_dna_sequences(self):
        """ Test Bloom filter with 50 DNA sequences. """
        dna_sequences = [generate_dna_sequence(50) for _ in range(50)]
        for dna in dna_sequences:
            self.bf.add(dna)
            self.assertTrue(self.bf.check(dna))
        self.assertFalse(self.bf.check(generate_dna_sequence(50)))

if __name__ == '__main__':
    unittest.main()
