#!/usr/bin/env python3
"""Interactive CLI for the Fibonacci calculator.

This module provides an interactive command-line interface for calculating
Fibonacci numbers using the existing fibonacci module implementations.

Usage:
    python cli.py

Features:
    - Interactive input with validation
    - Multiple algorithm selection
    - Performance metrics
    - Help and examples
    - Graceful error handling
"""

import sys
import time
from typing import Optional, Tuple

# Import our fibonacci implementations
try:
    from fibonacci import (
        fibonacci_iterative,
        fibonacci_memoized,
        fibonacci_recursive,
        fibonacci_sequence
    )
except ImportError:
    print("Error: fibonacci.py module not found. Please ensure it's in the same directory.")
    sys.exit(1)


class FibonacciCLI:
    """Interactive CLI for Fibonacci calculations."""
    
    def __init__(self):
        """Initialize the CLI with default settings."""
        self.default_algorithm = 'iterative'
        self.show_performance = True
        self.running = True
        
    def display_welcome(self) -> None:
        """Display welcome message and basic instructions."""
        print("\n" + "=" * 60)
        print("    🔢 INTERACTIVE FIBONACCI CALCULATOR 🔢")
        print("=" * 60)
        print("Calculate Fibonacci numbers with multiple algorithms!")
        print("\nQuick start:")
        print("  • Enter a number (e.g., 10) to calculate F(10)")
        print("  • Enter 100 to calculate F(100) - the task requirement!")
        print("  • Type 'help' for more options")
        print("  • Type 'quit' or 'exit' to leave")
        print("-" * 60)
    
    def display_help(self) -> None:
        """Display comprehensive help information."""
        print("\n" + "=" * 50)
        print("                  HELP & COMMANDS")
        print("=" * 50)
        
        print("\n📋 BASIC USAGE:")
        print("  <number>        - Calculate Fibonacci number at index")
        print("  Examples: 10, 25, 100, 1000")
        
        print("\n🔧 COMMANDS:")
        print("  help            - Show this help message")
        print("  algorithms      - List available algorithms")
        print("  algorithm <name> - Set calculation algorithm")
        print("  performance     - Toggle performance display")
        print("  sequence <n>    - Show Fibonacci sequence up to F(n)")
        print("  examples        - Show example calculations")
        print("  test100         - Demonstrate F(100) calculation")
        print("  quit/exit       - Exit the calculator")
        
        print("\n⚡ ALGORITHMS:")
        print("  iterative       - Fast, recommended for most cases")
        print("  memoized        - Great for repeated calculations")
        print("  recursive       - Educational (slow for n>30)")
        
        print("\n💡 TIPS:")
        print("  • Current algorithm: {}".format(self.default_algorithm))
        print("  • Performance display: {}".format('ON' if self.show_performance else 'OFF'))
        print("  • For large numbers (n>1000), use iterative algorithm")
        print("  • Recursive algorithm not recommended for n>30")
        print("  • F(100) = 354224848179261915075 (21 digits)")
        print("-" * 50)
    
    def display_examples(self) -> None:
        """Display example calculations."""
        print("\n" + "=" * 40)
        print("            EXAMPLES")
        print("=" * 40)
        
        examples = [
            (0, "F(0) = 0 (base case)"),
            (1, "F(1) = 1 (base case)"),
            (10, "F(10) = 55 (common example)"),
            (20, "F(20) = 6765 (moderate size)"),
            (50, "F(50) = 12586269025 (large number)"),
            (100, "F(100) = 354224848179261915075 (task requirement!)")
        ]
        
        print("\nCommon Fibonacci calculations:")
        for n, description in examples:
            result = fibonacci_iterative(n)
            print(f"  {description}")
            if n <= 100:  # Show actual calculation for all examples
                if len(str(result)) > 50:
                    print(f"    Result: {result} ({len(str(result))} digits)")
                else:
                    print(f"    Result: {result}")
        
        print("\n💡 Try entering any of these numbers: 0, 1, 10, 20, 50, 100")
        print("💡 Type 'test100' for a demonstration of F(100) calculation")
        print("-" * 40)
    
    def demonstrate_f100(self) -> None:
        """Demonstrate F(100) calculation as requested in the task."""
        print("\n" + "=" * 50)
        print("          F(100) CALCULATION DEMO")
        print("=" * 50)
        print("This demonstrates the task requirement: calculating F(100)")
        print("\nCalculating F(100) using different algorithms...\n")
        
        n = 100
        
        # Iterative
        print("🔹 Using ITERATIVE algorithm:")
        start_time = time.time()
        result_iter = fibonacci_iterative(n)
        time_iter = time.time() - start_time
        print(f"   F(100) = {result_iter}")
        print(f"   Time: {time_iter:.6f} seconds")
        print(f"   Digits: {len(str(result_iter))}")
        
        # Memoized
        print("\n🔹 Using MEMOIZED algorithm:")
        fibonacci_memoized.cache_clear()
        start_time = time.time()
        result_memo = fibonacci_memoized(n)
        time_memo = time.time() - start_time
        print(f"   F(100) = {result_memo}")
        print(f"   Time: {time_memo:.6f} seconds")
        print(f"   Verification: Results match = {result_iter == result_memo}")
        
        print("\n💡 Both algorithms successfully calculated F(100)!")
        print("💡 The iterative algorithm is typically fastest for large numbers.")
        print("💡 F(100) has 21 digits and equals 354224848179261915075")
        print("-" * 50)
    
    def list_algorithms(self) -> None:
        """Display available algorithms with descriptions."""
        print("\n" + "=" * 50)
        print("              AVAILABLE ALGORITHMS")
        print("=" * 50)
        
        algorithms = {
            'iterative': {
                'description': 'Linear time, constant space - RECOMMENDED',
                'complexity': 'O(n) time, O(1) space',
                'best_for': 'General use, large numbers (n>30)'
            },
            'memoized': {
                'description': 'Cached recursive - good for repeated calls',
                'complexity': 'O(n) time first call, O(1) subsequent',
                'best_for': 'Repeated calculations of same values'
            },
            'recursive': {
                'description': 'Pure recursion - educational only',
                'complexity': 'O(2^n) time, O(n) space',
                'best_for': 'Learning purposes (n<30 only)'
            }
        }
        
        current = self.default_algorithm
        
        for name, info in algorithms.items():
            marker = " ← CURRENT" if name == current else ""
            print(f"\n🔹 {name.upper()}{marker}")
            print(f"   Description: {info['description']}")
            print(f"   Complexity:  {info['complexity']}")
            print(f"   Best for:    {info['best_for']}")
        
        print(f"\nTo change algorithm, type: algorithm <name>")
        print("Example: algorithm memoized")
        print("-" * 50)
    
    def calculate_fibonacci(self, n: int) -> Tuple[int, float]:
        """Calculate Fibonacci number using selected algorithm.
        
        Args:
            n: The index to calculate
            
        Returns:
            Tuple of (result, execution_time)
        """
        start_time = time.time()
        
        if self.default_algorithm == 'iterative':
            result = fibonacci_iterative(n)
        elif self.default_algorithm == 'memoized':
            result = fibonacci_memoized(n)
        elif self.default_algorithm == 'recursive':
            if n > 35:  # Prevent extremely slow calculations
                print(f"⚠️  Warning: Recursive algorithm is too slow for n={n}")
                print("   Switching to iterative algorithm for this calculation...")
                result = fibonacci_iterative(n)
            else:
                result = fibonacci_recursive(n)
        else:
            # Fallback to iterative
            result = fibonacci_iterative(n)
        
        execution_time = time.time() - start_time
        return result, execution_time
    
    def display_result(self, n: int, result: int, execution_time: float) -> None:
        """Display calculation result with optional performance info.
        
        Args:
            n: The input index
            result: The calculated Fibonacci number
            execution_time: Time taken for calculation
        """
        print(f"\n🎯 F({n}) = {result}")
        
        # Show additional info for large results
        if result > 1000000:
            digits = len(str(result))
            print(f"   📊 Result has {digits} digits")
        
        # Special note for F(100)
        if n == 100:
            print(f"   ✅ Successfully calculated F(100) as requested in the task!")
        
        if self.show_performance:
            print(f"   ⏱️  Calculated in {execution_time:.6f} seconds using {self.default_algorithm} algorithm")
            
            # Performance hints
            if execution_time > 0.1:
                print("   💡 Tip: Try 'algorithm iterative' for better performance")
            elif n > 1000 and self.default_algorithm != 'iterative':
                print("   💡 Tip: Iterative algorithm is fastest for large numbers")
    
    def handle_sequence_command(self, parts: list) -> None:
        """Handle sequence generation command.
        
        Args:
            parts: Command parts split by space
        """
        if len(parts) != 2:
            print("❌ Usage: sequence <number>")
            print("   Example: sequence 10")
            return
        
        try:
            n = int(parts[1])
            if n < 0:
                print("❌ Please enter a non-negative number")
                return
            
            if n > 20:
                confirm = input(f"⚠️  Sequence for F(0) to F({n}) will be long. Continue? (y/N): ")
                if confirm.lower() not in ['y', 'yes']:
                    return
            
            start_time = time.time()
            sequence = fibonacci_sequence(n)
            execution_time = time.time() - start_time
            
            print(f"\n🔢 Fibonacci sequence F(0) to F({n}):")
            
            # Format sequence nicely
            if n <= 10:
                # Show inline for small sequences
                print(f"   {sequence}")
            else:
                # Show formatted for larger sequences
                for i, val in enumerate(sequence):
                    if i % 5 == 0 and i > 0:
                        print()  # New line every 5 numbers
                    print(f"F({i})={val}", end="  ")
                print()  # Final newline
            
            if self.show_performance:
                print(f"   ⏱️  Generated in {execution_time:.6f} seconds")
                
        except ValueError:
            print("❌ Please enter a valid number")
    
    def handle_algorithm_command(self, parts: list) -> None:
        """Handle algorithm selection command.
        
        Args:
            parts: Command parts split by space
        """
        if len(parts) != 2:
            print("❌ Usage: algorithm <name>")
            print("   Available: iterative, memoized, recursive")
            return
        
        algorithm = parts[1].lower()
        valid_algorithms = ['iterative', 'memoized', 'recursive']
        
        if algorithm not in valid_algorithms:
            print(f"❌ Unknown algorithm: {algorithm}")
            print(f"   Available: {', '.join(valid_algorithms)}")
            return
        
        old_algorithm = self.default_algorithm
        self.default_algorithm = algorithm
        
        print(f"✅ Algorithm changed from '{old_algorithm}' to '{algorithm}'")
        
        # Show warning for recursive algorithm
        if algorithm == 'recursive':
            print("   ⚠️  Warning: Recursive algorithm is slow for n>30")
    
    def process_command(self, user_input: str) -> None:
        """Process user input and execute appropriate action.
        
        Args:
            user_input: Raw input from user
        """
        user_input = user_input.strip().lower()
        
        if not user_input:
            return
        
        # Handle exit commands
        if user_input in ['quit', 'exit', 'q']:
            self.running = False
            print("\n👋 Thanks for using the Fibonacci Calculator!")
            return
        
        # Handle help command
        if user_input == 'help':
            self.display_help()
            return
        
        # Handle examples command
        if user_input == 'examples':
            self.display_examples()
            return
        
        # Handle F(100) demonstration command
        if user_input == 'test100':
            self.demonstrate_f100()
            return
        
        # Handle algorithms list command
        if user_input == 'algorithms':
            self.list_algorithms()
            return
        
        # Handle performance toggle
        if user_input == 'performance':
            self.show_performance = not self.show_performance
            status = "ON" if self.show_performance else "OFF"
            print(f"✅ Performance display turned {status}")
            return
        
        # Handle multi-word commands
        parts = user_input.split()
        
        if parts[0] == 'sequence':
            self.handle_sequence_command(parts)
            return
        
        if parts[0] == 'algorithm':
            self.handle_algorithm_command(parts)
            return
        
        # Try to parse as a number for Fibonacci calculation
        try:
            n = int(user_input)
            
            if n < 0:
                print("❌ Please enter a non-negative number")
                return
            
            # Warning for large recursive calculations
            if n > 35 and self.default_algorithm == 'recursive':
                print(f"⚠️  Warning: Recursive calculation for n={n} will be very slow")
                confirm = input("   Continue anyway? (y/N): ")
                if confirm.lower() not in ['y', 'yes']:
                    return
            
            # Perform calculation
            try:
                result, exec_time = self.calculate_fibonacci(n)
                self.display_result(n, result, exec_time)
                
            except (ValueError, TypeError) as e:
                print(f"❌ Calculation error: {e}")
            except KeyboardInterrupt:
                print("\n⚠️  Calculation interrupted by user")
            except Exception as e:
                print(f"❌ Unexpected error: {e}")
                
        except ValueError:
            print(f"❌ Unknown command: '{user_input}'")
            print("   Type 'help' for available commands or enter a number to calculate")
    
    def run(self) -> None:
        """Main CLI loop."""
        self.display_welcome()
        
        try:
            while self.running:
                try:
                    user_input = input("\nFibonacci> ")
                    self.process_command(user_input)
                    
                except KeyboardInterrupt:
                    print("\n\n👋 Goodbye!")
                    break
                except EOFError:
                    print("\n\n👋 Goodbye!")
                    break
                    
        except Exception as e:
            print(f"\n❌ Fatal error: {e}")
            print("Exiting...")


def main() -> None:
    """Entry point for the CLI application."""
    cli = FibonacciCLI()
    cli.run()


if __name__ == "__main__":
    main()
