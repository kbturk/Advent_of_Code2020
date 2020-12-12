import sys, itertools
from copy import deepcopy

from typing import Dict, List, Optional, Set, Tuple

def seat_count( row: int, col:int, l:List[List[str]] ) -> int:
    count = 0
    for delta_row in [-1, 0, 1]:
        for delta_col in [-1, 0, 1]:
            #pass if out of bounds.
            if row+delta_row < 0 or row+delta_row >= len(l):
                pass
            elif col+delta_col < 0 or col+delta_col >= len(l[0]):
                pass
            #pass if self
            elif (delta_col,delta_row) == (0,0):
                pass
            #otherwise count
            elif l[row+delta_row][col+delta_col] == '#':
                count += 1
    return count

def seat_move( HEIGHT: int, WIDTH: int, l:List[List[str]] ) -> List[List[str]]:
    l_next: List[List[str]] = deepcopy(l)
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if l[i][j] == 'L':
                count = seat_count(i,j,l)
                if count == 0:
                    l_next[i][j] = "#"
            elif l[i][j] == "#":
                count = seat_count(i,j,l)
                if count >= 4:
                    l_next[i][j] = "L"
            else:
                pass
    return l_next

def main(args: List[str]) -> int:
    with open(args[1], 'r') as f:
        l: List[List[str]] = [list(line.strip()) for line in f]

    HEIGHT, WIDTH = len(l), len(l[0])

    l_next: List[List[str]] = seat_move(HEIGHT,WIDTH,l)

    while l_next != l:
        l = deepcopy(l_next)
        l_next = seat_move(HEIGHT,WIDTH,l)

    count = 0
    for line in l:
        for c in line:
            if c == "#":
                count += 1
    print(count)
    return 0

if __name__ == '__main__':
    sys.exit( main( sys.argv ) )