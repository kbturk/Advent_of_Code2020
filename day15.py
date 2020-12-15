import sys, itertools, re
from copy import deepcopy

from typing import Dict, List, Optional, Set, Tuple


def main(args: List[str]) -> int:
    registrar: Dict[int,int]= {}

    with open(args[1], 'r') as f:
        input = [ int(c) for line in f for c in line.strip().split(',') ]
    print(input)

    simulation:Dict[int,int] = {}

    for i in range(len(input)):
        simulation[input[i]] = i

    print(simulation)

    next_entry = 0
    next_next_entry = 0

    for i in range(len(input),30000000):
        if next_entry in simulation.keys():
            next_next_entry = i - simulation[next_entry]
            simulation[next_entry] = i
            next_entry = deepcopy(next_next_entry)
        else:
            simulation[next_entry] = i
            next_entry = 0
        if i == 29999998:
            print(next_entry)

    return 0

if __name__ == '__main__':
    sys.exit( main( sys.argv ) )