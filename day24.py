import sys, re
from typing import Dict, List, Tuple, Set,Union
from copy import deepcopy
def the_crew_would_have_quit(tile_string:str) -> Tuple[int,int,int]:
    #coord = x,y,z
    coord = (0,0,0)
    #e,se,sw,w,nw,ne
    i = 0
    while i < len(tile_string):
        if tile_string[i] == "e":
            coord = (coord[0]+1,coord[1]-1,coord[2])
        elif tile_string[i] == "w":
            coord = (coord[0]-1,coord[1]+1,coord[2])
        elif tile_string[i] == "s":
            #se
            if tile_string[i+1] == "e":
                coord = (coord[0],coord[1]-1,coord[2]+1)
            #sw
            elif tile_string[i+1] == "w":
               coord = (coord[0]-1,coord[1],coord[2]+1)
            else:
                raise ValueError(f"something is wrong with the parse: {i},{tile_string}")
            #skip next index.
            i +=1
        elif tile_string[i] == "n":
            #ne
            if tile_string[i+1] == "e":
                coord = (coord[0]+1,coord[1],coord[2]-1)
            #nw
            elif tile_string[i+1] == "w":
               coord = (coord[0],coord[1]+1,coord[2]-1)
            else:
                raise ValueError(f"something is wrong with the parse: {i},{tile_string}")

            #skip next index.
            i +=1
        i +=1
        #print(f'i:{i},coord:{coord}')
    return coord

def black_surrounding_tiles(tile,black_tiles:List[Tuple[int,int,int]]) -> int:
    count = 0
    for i in [(0,1,-1),(1,0,-1),(1,-1,0),(0,-1,1),(-1,0,1),(-1,1,0)]:
        if (tile[0]+i[0],tile[1]+i[1],tile[2]+i[2]) in black_tiles:
            count += 1
    return count

def main() -> int:
    black_tiles: List[Tuple[int,int,int]] = []
    current_tile = (0,0,0)
    #part 1:
    for line in sys.stdin:
        tile_flip = the_crew_would_have_quit(line.strip())
        if tile_flip in black_tiles:
            black_tiles.remove(tile_flip)
        else:
            black_tiles.append(tile_flip)
    print(len(black_tiles))
    #part 2:
    tick = 0
    max_tick = 100
    next_tick_black_tiles: List[Tuple[int,int,int]] = deepcopy(black_tiles)

    while tick < max_tick:
        for tile in black_tiles:
            for i in [(0,1,-1),(1,0,-1),(1,-1,0),(0,-1,1),(-1,0,1),(-1,1,0),(0,0,0)]:
                check_tile = (tile[0]+i[0],tile[1]+i[1],tile[2]+i[2])
                black_tile_count = black_surrounding_tiles(check_tile,black_tiles)
                #if the tile is already black and
                #either has 0 surrounding black tiles or more than 2, remove.
                if check_tile in black_tiles:
                    if (black_tile_count == 0) or (black_tile_count > 2):
                        if check_tile in next_tick_black_tiles:
                            next_tick_black_tiles.remove(check_tile)
                else:
                    if black_tile_count == 2:
                        if check_tile not in next_tick_black_tiles:
                            next_tick_black_tiles.append(check_tile)
        tick += 1
        black_tiles = deepcopy(next_tick_black_tiles)
        print(tick,len(next_tick_black_tiles))
    return 0

if __name__ == '__main__':
    sys.exit(main())