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
    
def seat_count2( row: int, col:int, l:List[List[str]] ) -> int:
    up, down, left, right, lefttop, righttop, leftbottom, rightbottom = 0,0,0,0,0,0,0,0
    count:List[int] = []
    HEIGHT, WIDTH = len(l), len(l[0])
    #up
    for i in range(1,row+1):
        if l[row-i][col] == "#":
            up = 1
            break
        elif l[row-i][col] == "L":
            break
    #down
    for i in range(row+1,HEIGHT):
        if l[i][col] == "#":
            down = 1
            break
        elif l[i][col] == "L":
            break
    #left
    for i in range(1,col+1):
        if l[row][col-i] == "#":
            left = 1
            break
        elif l[row][col-i] == "L":
            break
    #right
    for i in range(col+1,WIDTH):
        if l[row][i] == "#":
            right = 1
            break
        elif l[row][i] == "L":
            break
            
    #left-top:
    for i in range(1,min([row,col])+1):
        if l[row-i][col-i] == "#":
            lefttop = 1
            break
        elif l[row-i][col-i] == "L":
            break

    #right-top:
    for i in range(1,min([row, WIDTH - col-1])+1):
        if l[row-i][col+i] == "#":
            righttop = 1
            break
        elif l[row-i][col+i] == "L":
            break

    #left-bottom:
    for i in range(1,min([HEIGHT-row-1,col])+1):
        if l[row+i][col-i] == "#":
            leftbottom = 1
            break
        elif l[row+i][col-i] == "L":
            break
    #right-bottom:
    for i in range(1,min([HEIGHT-row,WIDTH - col])):
        if l[row+i][col+i] == "#":
            rightbottom = 1
            break
        elif l[row+i][col+i] == "L":
            break
    count = [up, down, left, right, lefttop, righttop, leftbottom, rightbottom]
    return sum(count)

def seat_move( l:List[List[str]] ) -> List[List[str]]:
    l_next: List[List[str]] = deepcopy(l)
    HEIGHT, WIDTH = len(l), len(l[0])    
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if l[i][j] == 'L':
                count = seat_count2(i,j,l)
                if count == 0:
                    l_next[i][j] = "#"
            elif l[i][j] == "#":
                count = seat_count2(i,j,l)
                if count >= 5:
                    l_next[i][j] = "L"
            else:
                pass
    return l_next

def main(args: List[str]) -> int:
    with open(args[1], 'r') as f:
        l: List[List[str]] = [list(line.strip()) for line in f]

    HEIGHT, WIDTH = len(l), len(l[0])
    #initial state
    print('\n'.join("".join(line) for line in l))
    print()
    #first state, all full.
    l_next: List[List[str]] = seat_move(l)
    print('\n'.join(''.join(line) for line in l_next))
    print()
    print(f'seat count for: 0,2: {seat_count2(0,2,l_next)}')
    l_next = seat_move(l_next)
    print()
    #3rd state.
    print('\n'.join(''.join(line) for line in l_next))
    
    while l_next != l:
        l = deepcopy(l_next)
        l_next = seat_move(l)
        print()
        print('\n'.join(''.join(line) for line in l_next))
    count = 0
    for line in l:
        for c in line:
            if c == "#":
                count += 1
    print(count)
    
    return 0

if __name__ == '__main__':
    sys.exit( main( sys.argv ) )