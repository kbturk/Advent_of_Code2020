import sys, re
from typing import Dict, List, Tuple, Set,Union
from copy import deepcopy



def main() -> int:
    part = 2 #set to 1 or 2
    move = 0

    crab_cup: List[int] = [int(c) for line in sys.stdin for c in line.strip()]
    max_cup = max(crab_cup)
    current_cup = crab_cup[0]

    if part == 1:
        max_move = 100
        while move < max_move:
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
    #else part 2:
    else:
        max_move = 10000000
        #max_move = 6
        number_of_cups = 1000000
        cup_location = list(range(1,number_of_cups+2))
        cup_location[-1] = crab_cup[0]
        for i in range(len(crab_cup)-1):
            cup_location[crab_cup[i]] = crab_cup[(i+1)]
        cup_location[crab_cup[-1]] = len(crab_cup)+1
        
        #0 registry is special. It is the entrance into the list.
        cup_location[0] = 0
        #print(cup_location[:20])
        registry_location = crab_cup[0]
        while move < max_move:
            pick_1 = cup_location[registry_location]
            pick_2 = cup_location[pick_1]
            pick_3 = cup_location[pick_2]
            #print(f'pick up: {pick_1},{pick_2},{pick_3}')
            new_point = cup_location[pick_3]
            #print(f'registry_location {registry_location} will point to: {new_point}')
            next_registry = registry_location - 1
            while next_registry in [pick_1,pick_2,pick_3]:
                next_registry -= 1
            if next_registry < 1:
               next_registry = number_of_cups

            cup_location[pick_3] = cup_location[next_registry]
            cup_location[next_registry] = pick_1
            cup_location[registry_location] = new_point

            #print(f'destination: {next_registry}')
            #print()
            #print(f'cup locations: {cup_location[:20]}')
            move += 1
            registry_location = new_point
        print(f'cup locations: {cup_location[:20]}')
        #print(f'934001 is at: {cup_location.index(934001)}, 159792:{cup_location.index(159792)}')
        clock1 = cup_location[1]
        clock2 = cup_location[clock1]
        ans2 = clock1*clock2

        print(f'part 2 ans: {ans2},clock1:{clock1},clock2:{clock2}')
    return 0

if __name__ == '__main__':
    sys.exit(main())