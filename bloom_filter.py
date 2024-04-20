# bloom_filter.py
from bitarray import bitarray
import random

class BloomFilter:
    def __init__(self, size, hash_count, seeds=None):
        if size <= 0:
            raise ValueError("Size must be a positive integer")
        if hash_count <= 0:
            raise ValueError("Hash count must be a positive integer")
    
        self.size = size
        self.hash_count = hash_count
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)
        self.seed = seeds if seeds is not None else random.sample(range(1, 100), hash_count)  # Unique seeds for each hash function

    def _hash(self, item, seed):
        """Generate a hash for the given item using a seed."""
        hash_value = 0
        for char in item:
            hash_value = hash_value * 31 + ord(char)
        return (hash_value + seed) % self.size

    def add(self, item):
        for seed in self.seed:
            digest = self._hash(item, seed)
            self.bit_array[digest] = True

    def check(self, item):
        for seed in self.seed:
            digest = self._hash(item, seed)
            if not self.bit_array[digest]:
                return False
        return True
