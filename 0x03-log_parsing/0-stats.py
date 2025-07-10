#!/usr/bin/python3
"""Reads from standard input and computes metrics."""


import sys
import signal


status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
status_count = {code: 0 for code in status_codes}
total_size = 0
line_size = 0


def print_stats():
    """Print the stats that werecollected"""
    print(f"File sie: {total_size}")
    for code in sorted(status_count.keys()):
        if status_count[code]:
            print(f"{code}: {status_count[code]}")


try:
    for line in sys.stdin:
        parts = line.strip().split()

        if len(parts) < 7:
            continue

        status = parts[-2]
        file_size = parts[-1]

        try:
            total_size += int(file_size)
        except (ValueError, IndexError):
            continue

        if status in status_count:
            status_count[status] += 1

        line_count += 1
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    raise

# Print remaining stats if program ends/stops
print_stats()
