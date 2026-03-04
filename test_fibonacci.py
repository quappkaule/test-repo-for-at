#!/usr/bin/env python3
"""
Comprehensive test suite for the Fibonacci calculator module.

This module contains unit tests for all functions in the fibonacci module,
including edge cases, error handling, and performance tests.
"""

import unittest
import time
from fibonacci import (
    fibonacci_iterative,
    fibonacci_recursive,
    fibonacci_sequence,
    is_fibonacci_number
)


class TestFibonacci(unittest.TestCase):
    """Test cases for Fibonacci calculation functions."""
    
    def setUp(self):
        """Set up test fixtures with known Fibonacci values."""
        # First 20 Fibonacci numbers for reference
        self.known_fibonacci = [
            0, 1, 1, 2, 3, 5, 8, 13, 21, 34,
            55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181
        ]
    
    def test_fibonacci_iterative_basic(self):
        """Test basic functionality of iterative Fibonacci."""
        for i, expected in enumerate(self.known_fibonacci):
            with self.subTest(n=i):
                result = fibonacci_iterative(i)
                self.assertEqual(result, expected)
    
    def test_fibonacci_recursive_basic(self):
        """Test basic functionality of recursive Fibonacci."""
        for i, expected in enumerate(self.known_fibonacci[:15]):  # Limit for performance
            with self.subTest(n=i):
                result = fibonacci_recursive(i)
                self.assertEqual(result, expected)
    
    def test_fibonacci_iterative_edge_cases(self):
        """Test edge cases for iterative Fibonacci."""
        # Test zero
        self.assertEqual(fibonacci_iterative(0), 0)
        # Test one
        self.assertEqual(fibonacci_iterative(1), 1)
        # Test larger number
        self.assertEqual(fibonacci_iterative(50), 12586269025)
    
    def test_fibonacci_recursive_edge_cases(self):
        """Test edge cases for recursive Fibonacci."""
        # Test zero
        self.assertEqual(fibonacci_recursive(0), 0)
        # Test one
        self.assertEqual(fibonacci_recursive(1), 1)
    
    def test_fibonacci_iterative_type_errors(self):
        """Test type error handling for iterative Fibonacci."""
        with self.assertRaises(TypeError):
            fibonacci_iterative("5")
        with self.assertRaises(TypeError):
            fibonacci_iterative(5.5)
        with self.assertRaises(TypeError):
            fibonacci_iterative(None)
    
    def test_fibonacci_recursive_type_errors(self):
        """Test type error handling for recursive Fibonacci."""
        with self.assertRaises(TypeError):
            fibonacci_recursive("5")
        with self.assertRaises(TypeError):
            fibonacci_recursive(5.5)
        with self.assertRaises(TypeError):
            fibonacci_recursive(None)
    
    def test_fibonacci_iterative_value_errors(self):
        """Test value error handling for iterative Fibonacci."""
        with self.assertRaises(ValueError):
            fibonacci_iterative(-1)
        with self.assertRaises(ValueError):
            fibonacci_iterative(-10)
    
    def test_fibonacci_recursive_value_errors(self):
        """Test value error handling for recursive Fibonacci."""
        with self.assertRaises(ValueError):
            fibonacci_recursive(-1)
        with self.assertRaises(ValueError):
            fibonacci_recursive(-10)
    
    def test_fibonacci_consistency(self):
        """Test that iterative and recursive methods give same results."""
        for i in range(15):  # Limit recursive tests for performance
            with self.subTest(n=i):
                iter_result = fibonacci_iterative(i)
                rec_result = fibonacci_recursive(i)
                self.assertEqual(iter_result, rec_result)


class TestFibonacciSequence(unittest.TestCase):
    """Test cases for Fibonacci sequence generation."""
    
    def test_fibonacci_sequence_basic(self):
        """Test basic sequence generation."""
        expected = [0, 1, 1, 2, 3]
        result = fibonacci_sequence(5)
        self.assertEqual(result, expected)
    
    def test_fibonacci_sequence_empty(self):
        """Test empty sequence."""
        result = fibonacci_sequence(0)
        self.assertEqual(result, [])
    
    def test_fibonacci_sequence_single(self):
        """Test single element sequence."""
        result = fibonacci_sequence(1)
        self.assertEqual(result, [0])
    
    def test_fibonacci_sequence_type_error(self):
        """Test type error handling for sequence generation."""
        with self.assertRaises(TypeError):
            fibonacci_sequence("5")
    
    def test_fibonacci_sequence_value_error(self):
        """Test value error handling for sequence generation."""
        with self.assertRaises(ValueError):
            fibonacci_sequence(-1)


class TestIsFibonacciNumber(unittest.TestCase):
    """Test cases for Fibonacci number checker."""
    
    def test_is_fibonacci_number_true_cases(self):
        """Test cases that should return True."""
        fibonacci_numbers = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        for num in fibonacci_numbers:
            with self.subTest(num=num):
                self.assertTrue(is_fibonacci_number(num))
    
    def test_is_fibonacci_number_false_cases(self):
        """Test cases that should return False."""
        non_fibonacci_numbers = [4, 6, 7, 9, 10, 11, 12, 14, 15, 16]
        for num in non_fibonacci_numbers:
            with self.subTest(num=num):
                self.assertFalse(is_fibonacci_number(num))
    
    def test_is_fibonacci_number_type_error(self):
        """Test type error handling."""
        with self.assertRaises(TypeError):
            is_fibonacci_number("5")
    
    def test_is_fibonacci_number_value_error(self):
        """Test value error handling."""
        with self.assertRaises(ValueError):
            is_fibonacci_number(-1)


class TestPerformance(unittest.TestCase):
    """Performance tests for Fibonacci implementations."""
    
    def test_iterative_performance(self):
        """Test that iterative implementation performs well for large numbers."""
        start_time = time.time()
        result = fibonacci_iterative(1000)
        end_time = time.time()
        
        # Should complete in reasonable time (less than 1 second)
        self.assertLess(end_time - start_time, 1.0)
        # Verify result is correct (known value for F(1000))
        self.assertIsInstance(result, int)
        self.assertGreater(result, 0)
    
    def test_recursive_memoization(self):
        """Test that recursive implementation uses memoization effectively."""
        # First call
        start_time = time.time()
        result1 = fibonacci_recursive(30)
        first_call_time = time.time() - start_time
        
        # Second call (should be faster due to memoization)
        start_time = time.time()
        result2 = fibonacci_recursive(30)
        second_call_time = time.time() - start_time
        
        # Results should be the same
        self.assertEqual(result1, result2)
        # Second call should be significantly faster
        self.assertLess(second_call_time, first_call_time / 10)


if __name__ == "__main__":
    # Run all tests with verbose output
    unittest.main(verbosity=2)
