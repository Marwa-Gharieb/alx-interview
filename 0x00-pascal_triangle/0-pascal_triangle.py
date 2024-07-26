#!/usr/bin/python3
"""
pascal tringle
"""

def pascal_triangle(n):
    '''
    A func  returns a list of lists of integers representing the Pascal triangle of n
    '''

    if n <= 0:
        return []

    tringle = [[1]]
    for r in range(1, n):
        new = [1]
        prev = tringle[-1]

    for i in range(1, r):
        new.append(prev[i-1] + prev[i])

    new.append(1)
    tringle.append(new)

    return tringle
