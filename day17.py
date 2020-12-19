#Conway game of life!

import sys, itertools, re
from copy import deepcopy

from typing import Dict, List, Optional, Set, Tuple, Union

def evaluate_cell( cell: Tuple[ int, int, int ], universe: Set[ Tuple[ int, int, int ] ], i: int, j: int, k: int ) -> Set[ Tuple[ int, int, int] ]: 
    new_cells: Set[Tuple[ int, int, int ] ] = set()

    

    return new_cells

def main(args: List[str]) -> int:

    with open(args[1], 'r') as f:
        input = [ line.strip() for line in f ]

    #build the initial state of the universe:
    universe = set()
    #row,col,dim1:
    i,j,k,m = 0,0,0,0

    #populate the universe!
    for line in input:
        j = 0
        for c in line:
            if c == "#":
                universe.add((i,j,k,m))
            j+=1
        i += 1

    #advance the universe:
    tick = 0
    
    while tick <6:
        potential_new_neighbors = set()
        universe_next_tick = set()

        #print(f'old universe: \n{universe}\nstart of tick: {potential_new_neighbors}, {universe_next_tick}')

        for cell in universe:
            #At the start, assume each cell has 0 live neighbors:
            live_neighbors = 0

            for i in [-1,0,1]:
                for j in [-1,0,1]:
                    for k in [-1,0,1]:
                        for m in [-1,0,1]:
                            #add new empty cells to a potential live cell list.
                            if (cell[0] + i, cell[1] + j, cell[2] + k, cell[3] + m) not in universe:

                                potential_new_neighbors.add((cell[0] + i, cell[1] + j, cell[2] + k, cell[3] + m ))
                            #ignore itself.
                            if i == j == k == m == 0:
                                pass
                            elif (cell[0] + i, cell[1] + j, cell[2] + k, cell[3] + m) in universe:
                                live_neighbors += 1
            if (live_neighbors == 2) or (live_neighbors == 3):
                        universe_next_tick.add(cell)

        #print(f'after comparing old universe: {potential_new_neighbors}')
        #check those potential cells to become live cells.
        for cell in potential_new_neighbors:
            #At the start, assume each cell has 0 live neighbors:
            live_neighbors = 0

            for i in [-1,0,1]:
                for j in [-1,0,1]:
                    for k in [-1,0,1]:
                        for m in [-1,0,1]:
                            #ignore self.
                            if i == j == k == m == 0:
                                pass
                            elif (cell[0] + i, cell[1] + j, cell[2] + k, cell[3] + m ) in universe:
                                live_neighbors += 1
            if live_neighbors == 3:
                        universe_next_tick.add(cell)
        universe = deepcopy(universe_next_tick)
        #advance the universe
        tick += 1
        
       #print(f'tick = {tick}\n{universe}')

    print(len(universe))

    return 0

if __name__ == '__main__':
    sys.exit( main( sys.argv ) )