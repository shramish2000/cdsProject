import random
import string
import nltk
from nltk.corpus import words

nltk.download('words')

def generate_random_string(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

def generate_dna_sequence(length):
    return ''.join(random.choice('ACGT') for _ in range(length))

def generate_numeric_data(count):
    return [random.randint(1, 10000) for _ in range(count)]

def generate_natural_words(count):
    word_list = words.words()  # This includes over 236,000 English words
    return random.sample(word_list, count)

def generate_list_data(count):
    return [[generate_random_string(random.randint(5, 10)) for _ in range(random.randint(2, 5))] for _ in range(count)]
