#!/usr/bin/python3
"""A module that finds the perimeter of an island in a 2d matrix"""
def island_perimeter(grid):
    """
    A function that will find the perimeter of the island
    Args: List: grid
    Return: perimeter
    """
    perimeter = 0

    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == 1:
                # Top
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                # Bottom
                if i == len(grid) - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                # Left
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                # Right
                if j == len(row) - 1 or grid[i][j + 1] == 0:
                    perimeter += 1

    return perimeter
