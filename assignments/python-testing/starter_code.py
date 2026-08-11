"""Utility functions for the pytest assignment.

Students should NOT modify function names; only implement or use them when writing tests.
"""

from typing import List


def is_palindrome(s: str) -> bool:
    s_clean = ''.join(ch.lower() for ch in s if ch.isalnum())
    return s_clean == s_clean[::-1]


def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def unique_sorted(values: List[int]) -> List[int]:
    return sorted(set(values))


def flatten(nested: List[List[int]]) -> List[int]:
    return [x for row in nested for x in row]


__all__ = ["is_palindrome", "factorial", "unique_sorted", "flatten"]
