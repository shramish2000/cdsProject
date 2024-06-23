# Bloom Filter Project Documentation

## Overview

This project implements a Bloom Filter in Python. The code is organized into several files, each serving a specific purpose:

- `bloom_filter.py`: Contains the implementation of the Bloom Filter class.
- `data_generation.py`: Provides functions to generate various types of data for testing the Bloom Filter.
- `benchmark.py`: Benchmarks the performance of the Bloom Filter using different datasets and sizes.
- `test_bloom_filter.py`: Contains unit tests for the Bloom Filter implementation.
- `job_script.sh`: SLURM job script to run the benchmark on HPC infrastructure.

## How to Run

1. **Install Dependencies**:
    Ensure you have all necessary dependencies installed:
    ```bash
    pip install bitarray nltk matplotlib
    ```

2. **Run Unit Tests**:
    Use the following command to run the unit tests:
    ```bash
    python -m unittest test_bloom_filter.py
    ```

3. **Run Benchmarks**:
    Execute the benchmark script directly:
    ```bash
    python benchmark.py
    ```

4. **Run on HPC**:
    Submit the job script to your HPC scheduler:
    ```bash
    sbatch job_script.sh
    ```

## Detailed Implementation

### 1. Version Control and Collaboration

The code for bloom filter has been gradually developed with initial implementation, gradual addition of tests and regular commits. 

### 2. Bloom Filter Implementation

**Implementation Details:**

- The `BloomFilter` class in `bloom_filter.py` uses an object-oriented approach for better modularity and reusability.
- The constructor (`__init__`) initializes the bit array, the expected number of elements, and the number of hash functions.
- Four different hash functions (`_hash1`, `_hash2`, `_hash3`, `_hash4`) are used to reduce the probability of hash collisions.


### 3. Thorough Testing

**Testing Details:**

- The `test_bloom_filter.py` file contains comprehensive unit tests for the Bloom Filter implementation.
- The `setUp` method initializes a common Bloom Filter instance used across tests.

**Key Tests:**

- `test_add_and_check`: Verifies that an item added to the filter is subsequently recognized as present.
- `test_false_positive`: Ensures that items not added to the filter are generally recognized as absent, while acknowledging the possibility of false positives.
- `test_random_strings`, `test_dna_sequences`, `test_numbers`, `test_natural_words`, `test_list_data`: Test the filter with various data types to ensure robustness and versatility.

**Why This Approach?**

- **Coverage**: Tests cover various data types and scenarios to ensure the Bloom Filter works correctly in diverse situations.
- **False Positives**: Specific tests are designed to evaluate and ensure the false positive rate remains within acceptable limits.

### 4. Hash Functions

- Four different hash functions are implemented to ensure a robust Bloom Filter.
- These functions are tested for their effectiveness with different types of data in `test_bloom_filter.py`.

**Hash Functions:**

- `_hash1`: A variation of the popular DJB2 hash function which XORs each character.
- `_hash2`: Uses a simple polynomial accumulation for hashing in reverse order.
- `_hash3`: Employs a combination of bit shifting and addition, with enumeration to diversify results.
- `_hash4`: Utilizes multiplication and bitwise XOR operations for more randomness.
  
These hash functions were chosen for their simplicity and efficiency in terms of computation. They provide a good distribution of hash values, which is crucial for the performance of the Bloom Filter.

**Why These Hash Functions?**

- **Diversity**: Each hash function uses a different strategy to ensure a wide spread of hash values, minimizing collisions.
- **Efficiency**: These functions are computationally inexpensive, ensuring that the Bloom Filter operations remain fast.
- **Proven Effectiveness**: Variations of these functions are widely used in practice for their good distribution properties.

### 5. Time and Space Complexity

- The expected time complexity for insert and check operations is O(k), where k is the number of hash functions.
- The space complexity is O(m), where m is the size of the bit array.
- These complexities are discussed in the `benchmark.py` script, which includes performance tests.

### 6. Performance Testing

**Performance Evaluation:**

- The `benchmark.py` script evaluates the Bloom Filter's performance with different data sizes and types.
- `benchmark_bloom_filter` function measures insertion and checking times, false positive rates, compression rates, and memory usage.

**Steps Involved:**

1. **Insert Data**: Measure the time taken to insert elements into the Bloom Filter.
2. **Check Data**: Measure the time taken to check the presence of elements.
3. **False Positive Rate**: Calculate the false positive rate by comparing the Bloom Filter's responses against known data.
4. **Compression Rate**: Evaluate how well the Bloom Filter compresses the data compared to traditional storage.
5. **Memory Usage**: Track the memory used by the Bloom Filter.

**Why These Metrics?**

- **Insert/Check Times**: Critical for understanding the operational efficiency of the Bloom Filter.
- **False Positive Rate**: A key performance indicator, as Bloom Filters trade space efficiency for a controllable false positive rate.
- **Compression Rate**: Important for applications where memory usage is a constraint.
- **Memory Usage**: Provides insight into the actual memory footprint of the Bloom Filter.

### 7. False Positive Rate Analysis

**Analysis Details:**

- The false positive rate is analyzed as a function of the number of inserted elements.
- In `benchmark_bloom_filter`, detailed false positive rate calculations are performed at regular intervals of inserted elements.
- The false positive rate is calculated by comparing the filter’s responses with the actual membership of elements in the dataset.

**Why This Analysis?**

- **Accuracy**: Ensures the Bloom Filter performs within the expected false positive rate bounds.
- **Scalability**: Demonstrates how the false positive rate evolves as more elements are added, crucial for understanding the filter's scalability.

### 8. Compression Rate Analysis

**Analysis Details:**

- Compression rate is analyzed by comparing the bit array size to the size of traditional storage methods.
- `benchmark_bloom_filter` calculates the compression rate by evaluating the ratio of traditional storage bits to the bit array size.

**Why This Analysis?**

- **Efficiency**: Demonstrates the space efficiency of the Bloom Filter.
- **Applicability**: Helps in understanding how effective the Bloom Filter is in reducing memory usage compared to other storage methods.
