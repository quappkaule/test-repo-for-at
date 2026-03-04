"""Comprehensive tests for the Fibonacci module.

This module contains unit tests for all Fibonacci calculation functions,
including edge cases, error handling, and performance validation.
"""

import unittest
import time
from fibonacci import (
    fibonacci_recursive,
    fibonacci_iterative,
    fibonacci_memoized,
    fibonacci_sequence,
    fibonacci,
    _validate_input
)


class TestFibonacciBasic(unittest.TestCase):
    """Test basic functionality of Fibonacci functions."""
    
    # Known Fibonacci numbers for testing
    KNOWN_VALUES = [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (7, 13),
        (8, 21),
        (9, 34),
        (10, 55),
        (15, 610),
        (20, 6765),
    ]
    
    def test_fibonacci_recursive_known_values(self):
        """Test recursive implementation with known values."""
        for n, expected in self.KNOWN_VALUES[:11]:  # Limit to avoid slow tests
            with self.subTest(n=n):
                self.assertEqual(fibonacci_recursive(n), expected)
    
    def test_fibonacci_iterative_known_values(self):
        """Test iterative implementation with known values."""
        for n, expected in self.KNOWN_VALUES:
            with self.subTest(n=n):
                self.assertEqual(fibonacci_iterative(n), expected)
    
    def test_fibonacci_memoized_known_values(self):
        """Test memoized implementation with known values."""
        fibonacci_memoized.cache_clear()  # Clear cache before testing
        for n, expected in self.KNOWN_VALUES:
            with self.subTest(n=n):
                self.assertEqual(fibonacci_memoized(n), expected)
    
    def test_fibonacci_default_known_values(self):
        """Test default implementation with known values."""
        for n, expected in self.KNOWN_VALUES:
            with self.subTest(n=n):
                self.assertEqual(fibonacci(n), expected)


class TestFibonacciSequence(unittest.TestCase):
    """Test the Fibonacci sequence generation function."""
    
    def test_sequence_basic(self):
        """Test basic sequence generation."""
        expected_sequences = {
            0: [0],
            1: [0, 1],
            5: [0, 1, 1, 2, 3, 5],
            10: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55],
        }
        
        for n, expected in expected_sequences.items():
            with self.subTest(n=n):
                self.assertEqual(fibonacci_sequence(n), expected)
    
    def test_sequence_length(self):
        """Test that sequence has correct length."""
        for n in range(15):
            with self.subTest(n=n):
                sequence = fibonacci_sequence(n)
                self.assertEqual(len(sequence), n + 1)


class TestInputValidation(unittest.TestCase):
    """Test input validation and error handling."""
    
    def test_negative_input_error(self):
        """Test that negative inputs raise ValueError."""
        functions_to_test = [
            fibonacci_recursive,
            fibonacci_iterative,
            fibonacci_memoized,
            fibonacci_sequence,
            fibonacci,
        ]
        
        for func in functions_to_test:
            with self.subTest(func=func.__name__):
                with self.assertRaises(ValueError):
                    func(-1)
                with self.assertRaises(ValueError):
                    func(-10)
    
    def test_non_integer_input_error(self):
        """Test that non-integer inputs raise TypeError."""
        functions_to_test = [
            fibonacci_recursive,
            fibonacci_iterative,
            fibonacci_memoized,
            fibonacci_sequence,
            fibonacci,
        ]
        
        invalid_inputs = [1.5, "5", [5], None, True]
        
        for func in functions_to_test:
            for invalid_input in invalid_inputs:
                with self.subTest(func=func.__name__, input=invalid_input):
                    with self.assertRaises(TypeError):
                        func(invalid_input)
    
    def test_validate_input_function(self):
        """Test the internal validation function directly."""
        # Valid inputs should not raise exceptions
        for valid_input in [0, 1, 10, 100]:
            _validate_input(valid_input)  # Should not raise
        
        # Invalid inputs should raise exceptions
        with self.assertRaises(ValueError):
            _validate_input(-1)
        
        with self.assertRaises(TypeError):
            _validate_input(1.5)
        
        with self.assertRaises(TypeError):
            _validate_input("5")


class TestConsistency(unittest.TestCase):
    """Test that all implementations produce consistent results."""
    
    def test_implementations_consistency(self):
        """Test that all implementations give the same results."""
        test_values = [0, 1, 2, 5, 10, 15]  # Keep small for recursive
        
        for n in test_values:
            with self.subTest(n=n):
                fibonacci_memoized.cache_clear()
                
                recursive_result = fibonacci_recursive(n)
                iterative_result = fibonacci_iterative(n)
                memoized_result = fibonacci_memoized(n)
                default_result = fibonacci(n)
                
                # All should give the same result
                self.assertEqual(recursive_result, iterative_result)
                self.assertEqual(iterative_result, memoized_result)
                self.assertEqual(memoized_result, default_result)


class TestPerformance(unittest.TestCase):
    """Test performance characteristics of different implementations."""
    
    def test_iterative_performance(self):
        """Test that iterative implementation is reasonably fast."""
        n = 1000
        
        start_time = time.time()
        result = fibonacci_iterative(n)
        elapsed_time = time.time() - start_time
        
        # Should complete in reasonable time (< 0.01 seconds)
        self.assertLess(elapsed_time, 0.01)
        self.assertIsInstance(result, int)
        self.assertGreater(result, 0)
    
    def test_memoized_cache_effectiveness(self):
        """Test that memoization improves performance for repeated calls."""
        fibonacci_memoized.cache_clear()
        n = 100
        
        # First call - should populate cache
        start_time = time.time()
        result1 = fibonacci_memoized(n)
        first_call_time = time.time() - start_time
        
        # Second call - should use cache
        start_time = time.time()
        result2 = fibonacci_memoized(n)
        second_call_time = time.time() - start_time
        
        # Results should be the same
        self.assertEqual(result1, result2)
        
        # Second call should be much faster (cache hit)
        self.assertLess(second_call_time, first_call_time / 10)


class TestLargeNumbers(unittest.TestCase):
    """Test handling of large Fibonacci numbers."""
    
    def test_large_fibonacci_numbers(self):
        """Test calculation of large Fibonacci numbers."""
        # Test reasonably large numbers
        large_n = 100
        
        # These should not raise exceptions and should return integers
        result_iterative = fibonacci_iterative(large_n)
        result_memoized = fibonacci_memoized(large_n)
        
        self.assertIsInstance(result_iterative, int)
        self.assertIsInstance(result_memoized, int)
        self.assertEqual(result_iterative, result_memoized)
        self.assertGreater(result_iterative, 0)
    
    def test_sequence_large(self):
        """Test sequence generation for larger numbers."""
        n = 50
        sequence = fibonacci_sequence(n)
        
        self.assertEqual(len(sequence), n + 1)
        self.assertEqual(sequence[0], 0)
        self.assertEqual(sequence[1], 1)
        
        # Verify the Fibonacci property for the sequence
        for i in range(2, len(sequence)):
            self.assertEqual(sequence[i], sequence[i-1] + sequence[i-2])


if __name__ == "__main__":
    # Run all tests
    unittest.main(verbosity=2)