import sys, re
from typing import Dict, List, Tuple, Set,Union
from copy import deepcopy

def main() -> int:
    move = 0
    crab_cup: List[int] = [int(c) for line in sys.stdin for c in line.strip()]
    current_cup = crab_cup[0]

    while move < 100:
        cup_loc = crab_cup.index(current_cup)
        pick_up = []
        for i in range(1,4):
            pick_up.append(deepcopy(crab_cup[(cup_loc+i)%len(crab_cup)]))
        #print(f'pickup: {pick_up}')
        for i in range(0,3):
            crab_cup.remove(pick_up[i])
        try_cup = current_cup - 1

        while True:
            if try_cup in crab_cup:
                for j in range(len(pick_up)):
                    crab_cup.insert(crab_cup.index(try_cup)+1, pick_up[len(pick_up)-1-j])
                break
            elif try_cup < min(crab_cup):
                try_cup = max(crab_cup)
            else:
                try_cup -= 1

        #print(f'current cup: {current_cup}\npickup:{pick_up}\ndestination: {try_cup}\ncrab cup:{crab_cup}\n\n')
        move += 1
        current_cup = crab_cup[(crab_cup.index(current_cup)+1)%len(crab_cup)]
    one_spot = crab_cup.index(1)
    ultimate_cup = []
    for i in range(1,len(crab_cup)):
        ultimate_cup.append(crab_cup[(one_spot+i)%len(crab_cup)])

    print(f'crab cup: {crab_cup}, ultimate_cup: {ultimate_cup}')
    return 0

if __name__ == '__main__':
    sys.exit(main())