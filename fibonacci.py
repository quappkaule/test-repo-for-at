#!/usr/bin/env python3
"""
Fibonacci Calculator Module

This module provides efficient implementations for calculating Fibonacci numbers.
It includes both iterative and recursive approaches with proper error handling
and input validation.

Example:
    >>> from fibonacci import fibonacci_iterative, fibonacci_recursive
    >>> fibonacci_iterative(10)
    55
    >>> fibonacci_recursive(10)
    55
"""

from typing import Dict, Union
from functools import lru_cache


def fibonacci_iterative(n: int) -> int:
    """
    Calculate the nth Fibonacci number using an iterative approach.
    
    This is the recommended method for calculating Fibonacci numbers as it
    has O(n) time complexity and O(1) space complexity.
    
    Args:
        n (int): The position in the Fibonacci sequence (0-indexed)
        
    Returns:
        int: The nth Fibonacci number
        
    Raises:
        TypeError: If n is not an integer
        ValueError: If n is negative
        
    Examples:
        >>> fibonacci_iterative(0)
        0
        >>> fibonacci_iterative(1)
        1
        >>> fibonacci_iterative(10)
        55
    """
    if not isinstance(n, int):
        raise TypeError(f"Input must be an integer, got {type(n).__name__}")
    
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    if n <= 1:
        return n
    
    # Initialize first two Fibonacci numbers
    prev, curr = 0, 1
    
    # Calculate Fibonacci number iteratively
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    
    return curr


@lru_cache(maxsize=None)
def fibonacci_recursive(n: int) -> int:
    """
    Calculate the nth Fibonacci number using a recursive approach with memoization.
    
    This implementation uses Python's lru_cache decorator for memoization,
    which improves performance by caching previously computed values.
    Time complexity: O(n), Space complexity: O(n)
    
    Args:
        n (int): The position in the Fibonacci sequence (0-indexed)
        
    Returns:
        int: The nth Fibonacci number
        
    Raises:
        TypeError: If n is not an integer
        ValueError: If n is negative
        
    Examples:
        >>> fibonacci_recursive(0)
        0
        >>> fibonacci_recursive(1)
        1
        >>> fibonacci_recursive(10)
        55
    """
    if not isinstance(n, int):
        raise TypeError(f"Input must be an integer, got {type(n).__name__}")
    
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    if n <= 1:
        return n
    
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_sequence(n: int) -> list[int]:
    """
    Generate a list of the first n Fibonacci numbers.
    
    Args:
        n (int): Number of Fibonacci numbers to generate
        
    Returns:
        list[int]: List containing the first n Fibonacci numbers
        
    Raises:
        TypeError: If n is not an integer
        ValueError: If n is negative
        
    Examples:
        >>> fibonacci_sequence(5)
        [0, 1, 1, 2, 3]
        >>> fibonacci_sequence(0)
        []
    """
    if not isinstance(n, int):
        raise TypeError(f"Input must be an integer, got {type(n).__name__}")
    
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    if n == 0:
        return []
    
    sequence = []
    for i in range(n):
        sequence.append(fibonacci_iterative(i))
    
    return sequence


def is_fibonacci_number(num: int) -> bool:
    """
    Check if a given number is a Fibonacci number.
    
    A positive integer is a Fibonacci number if one or both of
    (5*n^2 + 4) or (5*n^2 - 4) is a perfect square.
    
    Args:
        num (int): The number to check
        
    Returns:
        bool: True if the number is a Fibonacci number, False otherwise
        
    Raises:
        TypeError: If num is not an integer
        ValueError: If num is negative
        
    Examples:
        >>> is_fibonacci_number(13)
        True
        >>> is_fibonacci_number(14)
        False
    """
    if not isinstance(num, int):
        raise TypeError(f"Input must be an integer, got {type(num).__name__}")
    
    if num < 0:
        raise ValueError("Input must be a non-negative integer")
    
    if num == 0:
        return True
    
    def is_perfect_square(n: int) -> bool:
        """Check if a number is a perfect square."""
        root = int(n ** 0.5)
        return root * root == n
    
    # A number is Fibonacci if one of 5*n^2 + 4 or 5*n^2 - 4 is a perfect square
    return (is_perfect_square(5 * num * num + 4) or 
            is_perfect_square(5 * num * num - 4))


if __name__ == "__main__":
    # Demo usage
    print("Fibonacci Calculator Demo")
    print("=" * 30)
    
    # Test basic functionality
    test_values = [0, 1, 5, 10, 15]
    
    print("\nIterative vs Recursive comparison:")
    for n in test_values:
        iter_result = fibonacci_iterative(n)
        rec_result = fibonacci_recursive(n)
        print(f"F({n}): Iterative = {iter_result}, Recursive = {rec_result}")
    
    # Generate sequence
    print(f"\nFirst 10 Fibonacci numbers: {fibonacci_sequence(10)}")
    
    # Test Fibonacci number checker
    print("\nFibonacci number checker:")
    test_numbers = [0, 1, 2, 3, 4, 5, 8, 13, 21, 22]
    for num in test_numbers:
        is_fib = is_fibonacci_number(num)
        print(f"{num} is {'a' if is_fib else 'not a'} Fibonacci number")
