# benchmark.py
import time
from bloom_filter import BloomFilter
from data_generation import generate_natural_words, generate_random_string, generate_numeric_data, generate_dna_sequence, generate_list_data

def time_function(func, *args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    return time.time() - start, result

def benchmark_bloom_filter(data_generator, num_samples, sizes, test_interval=100):
    insert_times = []
    check_times = []
    all_false_positive_rates = []
    compression_rates = []
    memory_usages = []

    for size in sizes:
        bf = BloomFilter(size * 10, size)
        sample_data = data_generator(size)
        test_data = data_generator(1000)  # Fixed number for check

        # Insert data
        insert_time, _ = time_function(lambda: [bf.add(item) for item in sample_data])
        insert_times.append(insert_time)

        # Check data
        check_time, _ = time_function(lambda: [bf.check(item) for item in test_data])
        check_times.append(check_time)

        # Detailed false positive rate analysis
        false_positive_rates = []
        for interval in range(test_interval, size + test_interval, test_interval):
            subset_data = sample_data[:interval]
            bf_subset = BloomFilter(interval * 10, interval)
            for item in subset_data:
                bf_subset.add(item)
            false_positives = sum(1 for item in test_data if bf_subset.check(item) and item not in subset_data)
            false_positive_rate = false_positives / len(test_data)
            false_positive_rates.append(false_positive_rate)
        all_false_positive_rates.append(false_positive_rates)

        # Compression rate
        bit_array_used = bf.bit_array.count(1)
        bit_array_size = len(bf.bit_array)
        traditional_storage_bits = len(sample_data) * 32
        compression_rate = traditional_storage_bits / bit_array_size
        compression_rates.append(compression_rate)

        # Memory usage
        memory_usages.append(bf.bit_array.buffer_info()[1])

    return sizes, insert_times, check_times, all_false_positive_rates, compression_rates, memory_usages



if __name__ == "__main__":
    sizes = [100, 500, 1000, 5000, 10000]
    data_generators = {
        'Random Strings': lambda count: [generate_random_string(10) for _ in range(count)],
        'DNA Sequences': lambda count: [generate_dna_sequence(10) for _ in range(count)],
        'Numbers': lambda count: generate_numeric_data(count),
        'Natural Words': lambda count: generate_natural_words(count),
        'List Data': lambda count: generate_list_data(count)
    }


