import unittest
from bloom_filter import BloomFilter
from data_generation import generate_random_string, generate_dna_sequence, generate_numeric_data, generate_natural_words, generate_list_data

class TestBloomFilter(unittest.TestCase):
    def setUp(self):
        self.size = 100000
        self.expected_elements = 500
        self.bf = BloomFilter(self.size, self.expected_elements)

    def test_add_and_check(self):
        """ Test adding items and checking their existence. """
        item = "test_item"
        self.assertFalse(self.bf.check(item), "Item should not be present initially.")
        self.bf.add(item)
        self.assertTrue(self.bf.check(item), "Item should be present after being added.")

    def test_false_positive(self):
        """ Test for false positives with random strings and DNA sequences. """
        self.bf.add("item1")
        self.assertFalse(self.bf.check("item2"), "False positive occurred.")

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

    def test_numbers(self):
        """ Test adding numbers and checking their existence. """
        numbers = generate_numeric_data(100)
        for number in numbers:
            self.assertFalse(self.bf.check(number))
            self.bf.add(number)
            self.assertTrue(self.bf.check(number))

    def test_natural_words(self):
        """ Test adding natural language words and checking their existence. """
        words = generate_natural_words(100)
        for word in words:
            self.assertFalse(self.bf.check(word))
            self.bf.add(word)
            self.assertTrue(self.bf.check(word))

    def test_list_data(self):
        """ Test adding lists of strings and checking their existence. """
        list_data = generate_list_data(50)
        for lst in list_data:
            list_str = '-'.join(lst)  # Convert list to a string representation for hashing
            self.assertFalse(self.bf.check(list_str))
            self.bf.add(list_str)
            self.assertTrue(self.bf.check(list_str))
            
    def test_collision_rate_for_strings(self):
        strings = [generate_random_string(20) for _ in range(1000)]
        self.run_collision_rate_test(strings, "random strings")

    def test_collision_rate_for_numbers(self):
        numbers = generate_numeric_data(1000)
        self.run_collision_rate_test(numbers, "numbers")

    def test_collision_rate_for_natural_words(self):
        words = generate_natural_words(1000)
        self.run_collision_rate_test(words, "natural words")

    def test_collision_rate_for_lists(self):
        lists = [str(lst) for lst in generate_list_data(1000)]
        self.run_collision_rate_test(lists, "lists")

    def run_collision_rate_test(self, items, description):
        hash_positions = set()
        total_positions = 0
        for item in items:
            for seed in range(self.bf.hash_count):
                position = self.bf._hash(str(item), seed)
                hash_positions.add(position)
                total_positions += 1
        collision_rate = 1 - len(hash_positions) / total_positions
        self.assertLess(collision_rate, 0.5, f"High collision rate detected for {description}.")

    def test_diversity_for_strings(self):
        strings = [generate_random_string(20) for _ in range(1000)]
        self.run_diversity_test(strings, "random strings")

    def test_diversity_for_numbers(self):
        numbers = generate_numeric_data(10)
        self.run_diversity_test(numbers, "numbers")

    def test_diversity_for_natural_words(self):
        words = generate_natural_words(10)
        self.run_diversity_test(words, "natural words")

    def test_diversity_for_lists(self):
        lists = [str(lst) for lst in generate_list_data(1000)]
        self.run_diversity_test(lists, "lists")

    def run_diversity_test(self, items, description):
        hash_positions = set()
        for item in items:
            for seed in range(self.bf.hash_count):
                position = self.bf._hash(str(item), seed)
                hash_positions.add(position)
        expected_unique_positions = min(self.size, int(len(items) * self.bf.hash_count * 0.9))
        self.assertTrue(len(hash_positions) >= expected_unique_positions, f"Not enough unique positions used for {description}.")

if __name__ == '__main__':
    unittest.main(exit=False)
