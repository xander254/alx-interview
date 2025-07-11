#!/usr/bin/python3
"""Utf8 validation"""


def validUTF8(data):
    """utf8 validation function"""
    remaining_bytes = 0

    for byte in data:
        byte = byte & 0xFF

        if remaining_bytes == 0:
            mask = 0b10000000
            while mask & byte:
                remaining_bytes += 1
                mask >>= 1

            if remaining_bytes == 0:
                continue

            if remaining_bytes == 1 or remaining_bytes > 4:
                return False

            remaining_bytes -= 1

        else:
            if not (byte & 0b10000000 and not (byte & 0b01000000)):
                return False
            remaining_bytes -= 1

    return remaining_bytes == 0
