import sys, itertools, re
from copy import deepcopy

from typing import Dict, List, Optional, Set, Tuple

         
def main(args: List[str]) -> int:
    registrar: Dict[int,int]= {}

    with open(args[1], 'r') as f:
        input = [ int(c) for line in f for c in line.strip().split(',') ]
    print(input)
    
    simulation = []
    
    for i in range(len(input)):
        simulation.append(input[i])

    

    for i in range(len(input),30000000):
        if simulation.count(simulation[-1]) > 1:
            #print(len(simulation),(simulation.index(simulation[-1])))
            simulation.append(int(len(simulation) -1 - simulation.index(simulation[-1])))
            #print(f'simulation after appending: {simulation}')
            simulation[simulation.index(simulation[-2])] = "X"
            #print(f'simulation after removal: {simulation}')
        else:
            simulation.append(0)
            #print(f'simulation after appending: {simulation}')
        #print(simulation)
    print(simulation[-1])
    return 0

if __name__ == '__main__':
    sys.exit( main( sys.argv ) )