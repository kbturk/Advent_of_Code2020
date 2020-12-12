import sys, itertools
from copy import deepcopy

from typing import Dict, List, Optional, Set, Tuple

def seat_count( row: int, col:int, d:Dict[Tuple[int,int], str] ) -> int:
    count = 0
    for delta_row in [-1, 0, 1]:
        for delta_col in [-1, 0, 1]:
            if (row+delta_row, col+delta_col) not in d.keys():
                pass
            elif d[(row+delta_row, col+delta_col)] == '#':
                count += 1
    return count

def seat_move( WIDTH: int, HEIGHT: int, d:Dict[Tuple[int,int],str]) -> Dict[Tuple[int,int],str]:
    d_next = deepcopy(d)

    for i in range(WIDTH):
        for j in range(HEIGHT):
            if d[(i,j)] == 'L':
                count = seat_count(i,j,d)
                if count == 0:
                    d_next[(i,j)] = "#"
            elif d[(i,j)] == "#":
                count = seat_count(i,j,d)
                if count >= 3:
                    d_next[(i,j)] = "L"
    return d_next
def main(args: List[str]) -> int:

    d: Dict[Tuple[int,int],str] = {}
    
    with open(args[1], 'r') as f:
        l = [c for line in f for c in line.strip().split()]
    HEIGHT, WIDTH = len(l), len(l[0])

    #char_list = [c for line in l for c in line]
    for i in range(WIDTH):
        for j in range(HEIGHT):
            d[(i,j)] = l[i][j]

    d = seat_move(WIDTH,HEIGHT,d)
    print(f'move 1: {d.values()}')
    d = seat_move(WIDTH,HEIGHT,d)
    print(f'move 2: {d.values()}')
    d = seat_move(WIDTH,HEIGHT,d)
    print(f'move 3: {d.values()}')
    
    return 0
    
if __name__ == '__main__':
    sys.exit( main( sys.argv ) )