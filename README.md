# Fibonacci Calculator

A comprehensive Python implementation for calculating Fibonacci numbers with multiple algorithms and thorough testing.

## Features

- **Multiple implementations**: Recursive, iterative, and memoized approaches
- **Type hints**: Full type annotation support
- **Comprehensive documentation**: Detailed docstrings and examples
- **Input validation**: Proper error handling for edge cases
- **Performance optimized**: Efficient algorithms for different use cases
- **Well tested**: Extensive unit test coverage

## Installation

No external dependencies required. Simply download the `fibonacci.py` file.

## Usage

### Basic Usage

```python
from fibonacci import fibonacci

# Calculate the 10th Fibonacci number
result = fibonacci(10)
print(result)  # Output: 55
```

### Different Implementations

```python
from fibonacci import (
    fibonacci_recursive,
    fibonacci_iterative, 
    fibonacci_memoized,
    fibonacci_sequence
)

# Recursive approach (slow for large numbers)
result = fibonacci_recursive(10)  # 55

# Iterative approach (recommended for most cases)
result = fibonacci_iterative(20)  # 6765

# Memoized approach (good for repeated calculations)
result = fibonacci_memoized(30)  # 832040

# Generate a sequence of Fibonacci numbers
sequence = fibonacci_sequence(10)  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
```

### Running the Demo

```bash
python fibonacci.py
```

This will run a demonstration showing different implementations and their performance.

## Implementation Details

### Algorithms

1. **Recursive** (`fibonacci_recursive`)
   - Time Complexity: O(2^n)
   - Space Complexity: O(n) 
   - Best for: Educational purposes, small numbers (n < 30)

2. **Iterative** (`fibonacci_iterative`)
   - Time Complexity: O(n)
   - Space Complexity: O(1)
   - Best for: Most general use cases, large numbers

3. **Memoized** (`fibonacci_memoized`) 
   - Time Complexity: O(n) first call, O(1) subsequent calls
   - Space Complexity: O(n)
   - Best for: Repeated calculations of the same values

### Input Validation

All functions include comprehensive input validation:
- Accepts only non-negative integers
- Raises `TypeError` for non-integer inputs
- Raises `ValueError` for negative inputs

## Testing

Run the comprehensive test suite:

```bash
python test_fibonacci.py
```

The test suite includes:
- **Basic functionality tests**: Verification against known Fibonacci values
- **Edge case handling**: Tests for invalid inputs and boundary conditions
- **Consistency tests**: Ensures all implementations produce identical results
- **Performance tests**: Validates reasonable execution times
- **Large number tests**: Handles computation of large Fibonacci numbers

### Test Coverage

- ✅ Known Fibonacci values (F(0) through F(20))
- ✅ Input validation and error handling
- ✅ Consistency across all implementations  
- ✅ Performance benchmarks
- ✅ Edge cases (0, 1, large numbers)
- ✅ Sequence generation validation

## Code Quality

This implementation follows Python best practices:

- **PEP 8 compliant**: Proper naming, spacing, and structure
- **Type hints**: Full type annotation support
- **Comprehensive docstrings**: Google-style documentation
- **Error handling**: Proper exception handling with descriptive messages
- **Modular design**: Separate functions for different approaches
- **Performance considerations**: Appropriate algorithm selection

## Performance Comparison

For reference, here are approximate performance characteristics:

| Algorithm | F(10) | F(20) | F(30) | F(100) |
|-----------|-------|-------|-------|--------|
| Recursive | ~0.0001s | ~0.002s | ~0.2s | ⚠️ Too slow |
| Iterative | ~0.00001s | ~0.00001s | ~0.00002s | ~0.0001s |
| Memoized | ~0.00001s | ~0.00001s | ~0.00002s | ~0.0001s |

**Note**: Recursive implementation has exponential time complexity and is not recommended for n > 30.

## Examples

### Calculate Single Fibonacci Number

```python
from fibonacci import fibonacci

# Calculate F(15)
result = fibonacci(15)
print(f"The 15th Fibonacci number is: {result}")  # 610
```

### Generate Fibonacci Sequence

```python
from fibonacci import fibonacci_sequence

# Generate first 10 Fibonacci numbers
sequence = fibonacci_sequence(9)
print(f"First 10 Fibonacci numbers: {sequence}")
# Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

### Performance Comparison

```python
import time
from fibonacci import fibonacci_iterative, fibonacci_memoized

n = 1000

# Time iterative approach
start = time.time()
result1 = fibonacci_iterative(n)
time1 = time.time() - start

# Time memoized approach  
start = time.time()
result2 = fibonacci_memoized(n)
time2 = time.time() - start

print(f"Iterative: {time1:.6f}s")
print(f"Memoized: {time2:.6f}s")
print(f"Results match: {result1 == result2}")
```

## Error Handling

```python
from fibonacci import fibonacci

# These will raise appropriate exceptions
try:
    fibonacci(-1)  # ValueError: Input must be non-negative
except ValueError as e:
    print(f"Error: {e}")

try:
    fibonacci("10")  # TypeError: Input must be an integer
except TypeError as e:
    print(f"Error: {e}")
```

## Contributing

To maintain code quality:
1. Follow PEP 8 style guidelines
2. Add type hints to all functions
3. Include comprehensive docstrings
4. Write tests for new functionality
5. Validate input parameters

## License

This implementation is provided as-is for educational and practical use.