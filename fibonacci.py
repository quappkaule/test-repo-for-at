"""Fibonacci number calculation module.

This module provides multiple implementations for calculating Fibonacci numbers,
including recursive, iterative, and memoized approaches.

Example:
    >>> from fibonacci import fibonacci_iterative
    >>> fibonacci_iterative(10)
    55
    
    >>> from fibonacci import fibonacci_memoized
    >>> fibonacci_memoized(20)
    6765
"""

from functools import lru_cache
from typing import Union


def fibonacci_recursive(n: int) -> int:
    """Calculate the nth Fibonacci number using recursion.
    
    This is the most intuitive implementation but has exponential time complexity.
    Not recommended for large values of n (n > 30).
    
    Args:
        n: The position in the Fibonacci sequence (0-indexed).
        
    Returns:
        The nth Fibonacci number.
        
    Raises:
        ValueError: If n is negative.
        TypeError: If n is not an integer.
        
    Examples:
        >>> fibonacci_recursive(0)
        0
        >>> fibonacci_recursive(1)
        1
        >>> fibonacci_recursive(5)
        5
        >>> fibonacci_recursive(10)
        55
    """
    _validate_input(n)
    
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_iterative(n: int) -> int:
    """Calculate the nth Fibonacci number using iteration.
    
    This implementation has linear time complexity and constant space complexity.
    Recommended for most use cases.
    
    Args:
        n: The position in the Fibonacci sequence (0-indexed).
        
    Returns:
        The nth Fibonacci number.
        
    Raises:
        ValueError: If n is negative.
        TypeError: If n is not an integer.
        
    Examples:
        >>> fibonacci_iterative(0)
        0
        >>> fibonacci_iterative(1)
        1
        >>> fibonacci_iterative(5)
        5
        >>> fibonacci_iterative(10)
        55
    """
    _validate_input(n)
    
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b


@lru_cache(maxsize=None)
def fibonacci_memoized(n: int) -> int:
    """Calculate the nth Fibonacci number using memoization.
    
    This implementation uses Python's built-in LRU cache for memoization,
    providing linear time complexity for repeated calls.
    
    Args:
        n: The position in the Fibonacci sequence (0-indexed).
        
    Returns:
        The nth Fibonacci number.
        
    Raises:
        ValueError: If n is negative.
        TypeError: If n is not an integer.
        
    Examples:
        >>> fibonacci_memoized(0)
        0
        >>> fibonacci_memoized(1)
        1
        >>> fibonacci_memoized(5)
        5
        >>> fibonacci_memoized(10)
        55
    """
    _validate_input(n)
    
    if n <= 1:
        return n
    return fibonacci_memoized(n - 1) + fibonacci_memoized(n - 2)


def fibonacci_sequence(n: int) -> list[int]:
    """Generate the first n+1 Fibonacci numbers as a list.
    
    Args:
        n: The highest position in the Fibonacci sequence to calculate.
        
    Returns:
        A list containing Fibonacci numbers from F(0) to F(n).
        
    Raises:
        ValueError: If n is negative.
        TypeError: If n is not an integer.
        
    Examples:
        >>> fibonacci_sequence(5)
        [0, 1, 1, 2, 3, 5]
        >>> fibonacci_sequence(0)
        [0]
    """
    _validate_input(n)
    
    if n == 0:
        return [0]
    
    sequence = [0, 1]
    for i in range(2, n + 1):
        sequence.append(sequence[i - 1] + sequence[i - 2])
    
    return sequence


def _validate_input(n: Union[int, float]) -> None:
    """Validate input for Fibonacci functions.
    
    Args:
        n: The input value to validate.
        
    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is negative.
    """
    if not isinstance(n, int):
        raise TypeError(f"Input must be an integer, got {type(n).__name__}")
    
    if n < 0:
        raise ValueError("Input must be non-negative")


# Convenience function - defaults to the most efficient implementation
def fibonacci(n: int) -> int:
    """Calculate the nth Fibonacci number (default implementation).
    
    This function uses the iterative approach as it provides the best
    balance of performance and memory usage for most use cases.
    
    Args:
        n: The position in the Fibonacci sequence (0-indexed).
        
    Returns:
        The nth Fibonacci number.
        
    Examples:
        >>> fibonacci(10)
        55
        >>> fibonacci(20)
        6765
    """
    return fibonacci_iterative(n)


if __name__ == "__main__":
    # Example usage and simple performance comparison
    import time
    
    print("Fibonacci Calculator Demo")
    print("=" * 25)
    
    # Test basic functionality
    n = 10
    print(f"\nFibonacci number at position {n}:")
    print(f"Recursive: {fibonacci_recursive(n)}")
    print(f"Iterative: {fibonacci_iterative(n)}")
    print(f"Memoized:  {fibonacci_memoized(n)}")
    
    # Show sequence
    print(f"\nFirst {n+1} Fibonacci numbers:")
    print(fibonacci_sequence(n))
    
    # Simple performance comparison for larger number
    n_large = 25
    print(f"\nPerformance comparison for F({n_large}):")
    
    # Time iterative
    start = time.time()
    result_iter = fibonacci_iterative(n_large)
    time_iter = time.time() - start
    print(f"Iterative: {result_iter} (Time: {time_iter:.6f}s)")
    
    # Time memoized
    fibonacci_memoized.cache_clear()  # Clear cache for fair comparison
    start = time.time()
    result_memo = fibonacci_memoized(n_large)
    time_memo = time.time() - start
    print(f"Memoized:  {result_memo} (Time: {time_memo:.6f}s)")
    
    print("\nNote: Recursive implementation not tested for large n due to exponential time complexity.")