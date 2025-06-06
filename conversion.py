"""
Module: conversion
Converts a decimal number from range (0, 100) to binary format
"""


def decimal_to_binary(n: int) -> str:
    """
    Returns:
        str: Binary representation of n.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is outside the range [0, 100].
    """
    if not isinstance(n, int):
        raise TypeError(f"Input must be an integer, got {type(n).__name__!r}")
    if n < 0 or n > 100:
        raise ValueError("Input must be between 0 and 100 inclusive")

    # Using Python built-in bin and strip the '0b' prefix
    return bin(n)[2:]
