import sys, itertools
from copy import deepcopy

from typing import Dict, List, Optional, Set, Tuple

def rick_roll_parse(command:str,instr:int,x:int,y:int,facing:str) -> Tuple[Tuple[int,int],str]:
    turn_left: Dict = {'N':'W','W':'S','S':'E','E':'N'}
    turn_right: Dict = {'N':'E','E':'S','S':'W','W':'N'}
    if command == "N":
        return (x,y-instr),facing
    if command == "S":
        return (x,y+instr),facing
    if command == "E":
        return (x+instr,y),facing
    if command == "W":
        return (x-instr,y),facing
    if command == "L":
        if instr%90 != 0:
            raise ValueError
        turns = instr//90
        for i in range(turns):
            facing = turn_left[facing]
        return (x,y),facing
    if command == "R":
        if instr%90 != 0:
            raise ValueError
        turns = instr//90
        for i in range(turns):
            facing = turn_right[facing]
        return (x,y),facing
    if command == "F":
        if facing == "N":
            return (x,y-instr),facing
        if facing == "S":
            return (x,y+instr),facing
        if facing == "E":
            return (x+instr,y),facing
        if facing == "W":
            return (x-instr,y),facing

    print("did not find a match. Check input.")
    return (x,y), facing

def main(args: List[str]) -> int:
    with open(args[1], 'r') as f:
        l = [[l[0],int(l[1:])] for line in f for l in line.strip().split()]
    print(f'{l}')

    x,y, facing = 0,0, 'E'
    for instructions in l:
        (x,y), facing = rick_roll_parse(instructions[0],instructions[1],x,y,facing)
        print(f'{x},{y}: {facing}')
    print(f'ans: {abs(x)+abs(y)}')
    return 0

if __name__ == '__main__':
    sys.exit( main( sys.argv ) )