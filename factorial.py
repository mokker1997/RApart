# coding: utf-8
"""Utility for factorial calculation."""


def factorial(n):
    """Return the factorial of a non-negative integer n."""
    if n < 0:
        raise ValueError("n must be non-negative")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    import sys
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    print(factorial(n))
