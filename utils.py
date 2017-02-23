# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 17:16:43 2017

@author: prade_000
"""

rows = 'ABCDEFGHI'
cols = '123456789'

def cross(a, b):
    return [s+t for s in a for t in b]

boxes = cross(rows, cols)

row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
# create diagonal units. adding these to the units automaticlly applies all constrains on them
diagonal_units =[]
diagonal_units1 =[]
diagonal_units2 =[]
for i in (range(9)):
    diagonal_units1.append(rows[i]+cols[i])
    diagonal_units2.append(rows[i]+str(9-i))
diagonal_units.append(diagonal_units1)
diagonal_units.append(diagonal_units2)
unitlist = row_units + column_units + square_units+ diagonal_units
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)

def display(values):
    """
    Display the values as a 2-D grid.
    Input: The sudoku in dictionary form
    Output: None
    """
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    return