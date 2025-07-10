#!/usr/bin/python3
"""A module to check if boxes can be unlocked or not"""


def canUnlockAll(boxes):
    """A func that checks if boxes can be unlocked"""
    if not boxes or not isinstance(boxes, list):
        return False

    n = len(boxes)
    opened = set([0])
    stack = [0]     

    while stack:
        current = stack.pop()

        for key in boxes[current]:
            if isinstance(key, int) and 0 <= key < n and key not in opened:
                opened.add(key)
                stack.append(key)

    return len(opened) == n
    