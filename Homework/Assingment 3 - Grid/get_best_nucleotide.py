"""
File: get_best_nucleotide.py
--------------
ADD YOUR DESCRIPTION HERE
"""
import os
import sys

from TextGrid import TextGrid, Cell


def get_best_nucleotide(nucleotide1, nucleotide2, nucleotide3):
    """
    Given three nucleotides, returns a nucleotide with the most common *non-blank* value. If multiple nucleotides have the same value, it doesn't matter which specific nucleotide is returned so long as its value is correct. You can assume there will never be ambiguity -- there will always be a clear majority non-blank character.

    Input:
        three nucleotides (Cells) to be compared
    Returns:
        best (Cell): nucleotide with most common non-blank value

    This doctest creates nucleotides for simple tests.
    >>> grid = TextGrid('ATCG_.txt')
    >>> A = grid.get_cell(0,0)
    >>> T = grid.get_cell(1,0)
    >>> C = grid.get_cell(2,0)
    >>> G = grid.get_cell(3,0)
    >>> blank = grid.get_cell(4,0)
    >>> best1 = get_best_nucleotide(A, A, A)
    >>> best1.value
    'A'
    >>> best2 = get_best_nucleotide(A, T, T)
    >>> best2.value
    'T'
    >>> best3 = get_best_nucleotide(A, blank, A)
    >>> best3.value
    'A'
    >>> best4 = get_best_nucleotide(blank, blank, T)
    >>> best4.value
    'T'
    """
    grid = TextGrid.blank(1, 1)
    value1 = 0
    value2 = 0
    value3 = 0
    value4 = 0
    lst = [nucleotide1, nucleotide2, nucleotide3]
    for i in lst:
        if i.value == 'A':
            value1 += 1
        elif i.value == 'T':
            value2 += 1
        elif i.value == 'C':
            value3 += 1
        elif i.value == 'G':
            value4 += 1

    Tv = {'A': value1, 'T': value2, 'C': value3, 'G': value4}

    Keymax = max(Tv, key=Tv.get)
    for y in range(grid.height):
        # loop over all the rows
        for x in range(grid.width):
            myCell = grid.get_cell(x, y)
    myCell.value = Keymax
    return myCell

######## DO NOT MODIFY ANY CODE BELOW THIS LINE ###########


def main():
    n1 = get_valid_nucleotide()
    n2 = get_valid_nucleotide()
    n3 = get_valid_nucleotide()
    best = get_best_nucleotide(n1, n2, n3)
    print("The best nucleotide of", n1, n2, n3, "is", best.value)


VALID_NUCLEOTIDES = {'A', 'T', 'C', 'G', '_'}


def get_valid_nucleotide():
    nuc = input("Enter a nucleotide (A, T, C, or G): ").strip().upper()
    while nuc not in VALID_NUCLEOTIDES:
        print("Invalid entry.")
        nuc = input("Enter a nucleotide (A, T, C, or G): ").strip().upper()
    cell = Cell(nuc, 0, 0)
    return cell


if __name__ == '__main__':
    main()
