#!/usr/bin/python3
"""Minimum operations"""


def minOperations(n):
    """Minimum operations"""
    if n < 2:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n = n // factor
        factor += 1

    return operations
