#!/usr/bin/python3
"""Solves the N Queens problem"""


import sys


def is_safe(row, col, queens):
    """check if num is safe"""
    for r, c in queens:
        if c == col or abs(row - r) == abs(col - c):
            return False
    return True


def solve_nqueens(n, row=0, queens=[], solutions=[]):
    """slve n queen"""
    if row == n:
        solutions.append(queens[:])
        return

    for col in range(n):
        if is_safe(row, col, queens):
            queens.append([row, col])
            solve_nqueens(n, row + 1, queens, solutions)
            queens.pop()


def main():
    """Main func program starts here"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    solve_nqueens(n, 0, [], solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
