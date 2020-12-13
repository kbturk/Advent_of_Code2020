import sys, itertools
from copy import deepcopy

from typing import Dict, List, Optional, Set, Tuple

def rick_roll_parse(command:str,instr:int,x:int,y:int, facing:str) -> Tuple[Tuple[int,int],str]:
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

def never_going_to_give_you_up_parse(command:str,instr:int,waypoint_x:int, waypoint_y:int,
                                    x:int,y:int) -> Tuple[Tuple[int,int],Tuple[int,int]]:
    if command == "N":
        return (waypoint_x,waypoint_y-instr),(x,y)
    if command == "S":
        return (waypoint_x,waypoint_y+instr),(x,y)
    if command == "E":
        return (waypoint_x+instr,waypoint_y),(x,y)
    if command == "W":
        return (waypoint_x-instr,waypoint_y),(x,y)

    if command == "L":
        if instr%90 != 0:
            raise ValueError
        turns = instr//90
        while turns != 0:
            waypoint_x,waypoint_y = waypoint_y, - waypoint_x
            turns -= 1
        return (waypoint_x,waypoint_y), (x,y)

    if command == "R":
        if instr%90 != 0:
            raise ValueError
        turns = instr//90
        while turns != 0:
            waypoint_x,waypoint_y = - waypoint_y, waypoint_x
            #print(waypoint_x, waypoint_y)
            turns -= 1
        return (waypoint_x,waypoint_y), (x,y)

    if command == "F":
            return (waypoint_x,waypoint_y),(x+waypoint_x*instr,y+waypoint_y*instr)

    print("did not find a match. Check input.")
    return (waypoint_x,waypoint_y), (x,y)

def main(args: List[str]) -> int:
    with open(args[1], 'r') as f:
        l = [[l[0],int(l[1:])] for line in f for l in line.strip().split()]
    #print(f'{l}')

    x,y, facing = 0,0, 'E'
    for instructions in l:
        (x,y), facing = rick_roll_parse(instructions[0],instructions[1],x,y,facing)
        #print(f'{x},{y}: {facing}')
    print(f'part 1 ans: {abs(x)+abs(y)}')

    waypoint_x,waypoint_y,x,y = 10,-1,0,0
    for instructions in l:
        (waypoint_x,waypoint_y), (x,y) = never_going_to_give_you_up_parse(
                                         instructions[0],instructions[1],waypoint_x,waypoint_y,x,y)
        print(f'waypoint: {waypoint_x},{waypoint_y} boat: {x},{y}')
    print(f'part 2 ans: {abs(x)+abs(y)}')
    return 0

if __name__ == '__main__':
    sys.exit( main( sys.argv ) )