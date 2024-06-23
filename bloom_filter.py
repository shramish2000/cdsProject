# bloom_filter.py: implementation of the Bloom Filter class.

from bitarray import bitarray

class BloomFilter:
    def __init__(self, size, expected_elements):
        self.size = size
        self.expected_elements = expected_elements
        self.hash_count = 4  
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)

    def _hash1(self, item):
        hash_value = 5381
        for char in str(item):
            hash_value = (hash_value * 33) ^ ord(char)
        return hash_value % self.size

    def _hash2(self, item):
        hash_value = 0
        for char in reversed(str(item)):
            hash_value = (hash_value * 31) + ord(char)
        return hash_value % self.size

    def _hash3(self, item):
        hash_value = 7
        for i, char in enumerate(str(item)):
            hash_value = hash_value * 31 + (ord(char) << (i % 4))
        return hash_value % self.size

    def _hash4(self, item):
        hash_value = 0
        for char in str(item):
            hash_value = (hash_value * 29) + ord(char)
            hash_value ^= hash_value >> 3
        return hash_value % self.size

    def _hash(self, item, seed):
        if seed == 0:
            return self._hash1(item)
        elif seed == 1:
            return self._hash2(item)
        elif seed == 2:
            return self._hash3(item)
        elif seed == 3:
            return self._hash4(item)

    def add(self, item):
        for seed in range(self.hash_count):
            digest = self._hash(item, seed)
            self.bit_array[digest] = True

    def check(self, item):
        return all(self.bit_array[self._hash(item, seed)] for seed in range(self.hash_count))

