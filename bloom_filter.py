# bloom_filter.py
import random

class BloomFilter:
    def __init__(self, size, hash_count):
        self.size = size
        self.hash_count = hash_count
        self.seed = random.sample(range(1, 100), hash_count)  # Unique seeds for each hash function

    def _hash(self, item, seed):
        """Generate a hash for the given item using a seed."""
        hash_value = 0
        for char in item:
            hash_value = hash_value * 31 + ord(char)
        return (hash_value + seed) % self.size