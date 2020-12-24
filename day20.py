#Tessellate matching game. Assumes a list of tiles of 10x10.

import sys, re
from typing import Sequence, Optional, Dict, Pattern, Tuple, List
from copy import deepcopy

def flip_horizontal(tile_stuff:List[str]) -> List[str]:
    #
    #before
    #abaa      0,1,2,3
    #bbcb  ->4,5,6,7
    #cddc  ->8,9,10,11
    #deed     12,13,14,15
    #
    #after
    #deed     12,13,14,15
    #cddc  ->8,9,10,11
    #bbcb  ->4,5,6,7
    #abaa      0,1,2,3
    #
    #new top = bottom
    #reverse right
    #reverse left
    #new bottom = top
    #
    new_body = ''
    body = tile_stuff[4]
    #print("flipping body vertically:")
    for i in range(0,8):
        new_body += body[64-(i*8+8):64-i*8]
        #print(new_body[i*8:i*8+8])
    #print()
    #print(f'body len: {len(new_body)}, {len(body)}')
    #0 ,  1   ,    2     ,3   ,   4
    top,right,bottom,left,body = tile_stuff[2],tile_stuff[1][::-1],tile_stuff[0],tile_stuff[3][::-1],new_body
    #print(f'{top}\n{right}\n{bottom}\n{left}')
    return [top,right,bottom,left,body]

def flip_vertical(tile_stuff:List[str]) -> List[str]:
    #
    #before
    #abaa      0,1,2,3
    #bbcb  ->4,5,6,7
    #cddc  ->8,9,10,11
    #deed     12,13,14,15
    #
    #after
    #reverse top
    #new right = left
    #reverse bottom
    #new left = right
    #new body is reversed every 8 groups.
    new_body = ''
    body = tile_stuff[4]
    for i in range(0,8):
        new_body += body[i*8:i*8+8][::-1]
        #print(new_body[i*8:i*8+8])
    #print()
    #print(f'body len: {len(new_body)}, {len(body)}')
    #0 ,  1   ,    2     ,3   ,   4
    top,right,bottom,left,body = tile_stuff[0][::-1],tile_stuff[3],tile_stuff[2][::-1],tile_stuff[1],new_body
    #print(f'{top}\n{right}\n{bottom}\n{left}')
    return [top,right,bottom,left,body]

def rotate_right(tile_stuff:List[str]) -> List[str]:
    #
    #before
    #abaa      0,1,2,3
    #bbcb  ->4,5,6,7
    #cddc  ->8,9,10,11
    #deed     12,13,14,15
    #
    #after:
    #dcba      12,8,4,0
    #edbb  ->13,9,5,1
    #edca  ->14,10,6,2
    #dcba      15,11,7,3
    #
    #
    #in summary:
    #new top = old left, reversed
    #new right = old top
    #new bottom = old right, reversed
    #new left = old bottom
    #new body: (8x8 square)
    #body[8*7+i]+body[8*6+i]+body[8*5+i]+body[8*4+i]+body[8*3+i]+body[8*2+i]+body[8+i]+body[0+i]
    new_body = ""
    body = tile_stuff[4]
    for i in range(0,8):
        new_body += body[8*7+i]+body[8*6+i]+body[8*5+i]+body[8*4+i]+\
        body[8*3+i]+body[8*2+i]+body[8+i]+body[0+i]
        #print(new_body[i*8:i*8+8])
    #0 ,  1   ,    2     ,3   ,   4
    top,right,bottom,left,body = tile_stuff[3][::-1], tile_stuff[0], tile_stuff[1][::-1], tile_stuff[2],new_body
    #print(f'{top}\n{right}\n{bottom}\n{left}')
    return [top,right,bottom,left,body]

def match(tile_name, tile:Dict[int,List[str]]) -> Tuple[int,List[str]]:
    matches_found = 0
    not_matched = list(tile[tile_name][0:4])
    for keys in tile.keys():
        if keys == tile_name:
            pass
        else:
            
            #print(f'checking {tile_name} & {keys}')
            for i in range(0,4):
                for j in range(0,4):
                    if tile[keys][j] == tile[tile_name][i]:
                        matches_found += 1
                        #print(f'{tile_name} & {keys} share a side: {tile[tile_name][i]} & {tile[keys][j]}')
                        not_matched.remove(tile[tile_name][i])
                    elif tile[keys][j][::-1] == tile[tile_name][i]:
                        matches_found += 1
                        #print(f'{tile_name} & {keys} share a side: {tile[tile_name][i]} & {tile[keys][j]}')
                        not_matched.remove(tile[tile_name][i])
    #print(f'Number of matches found: {matches_found}, sides not matched: {not_matched}')
    return matches_found, not_matched

def parse_it() -> Dict[int,List[str]]:
    tile: Dict[int,List[str]] = {}
    tile_name = 0
    
    #sides
    top,right,bottom,left = "","","",""
    #body
    body = ""
    for line in sys.stdin:
        line = line.rstrip()
        check1 = re.fullmatch(r'Tile ([0-9]+):',line)
        if check1:
            
            tile_name = int(check1.group(1))
            #sides
            top,right,bottom,left = "","","",""
            #body: should be 81 char long, or 9x9 rec.
            body = ""

        elif line =="":
            body = body[11:19]+body[21:29]+body[31:39]+body[41:49]+\
                        body[51:59]+body[61:69]+body[71:79]+body[81:89]
            #print(tile_name)
            #for l in range(0,len(body),8):
            #    print(f'{body[l:l+8]}')
            #print()
            tile[tile_name] = [top,right,bottom,left,body]

        elif ("\#" or "\." in line) and top == "":
            top = line
            right = line[len(line)-1]
            left = line[0]
            body = line

        elif "\#" or "\." in line:
            right = right + line[len(line)-1]
            left = left + line[0]
            bottom = line
            body = body+line
    return tile

#returns the next match key where the next tile's right side matches the right side of the previous key. 
#It actually needs to be the left, so that's corrected in the return.
def right_match(match_side: str, tile: Dict[int,List[str]]) ->Tuple[int,List[str]]:
    for key in tile.keys():
        #if it's a perfect match, return it.
        if match_side == tile[key][1]:
            return key, tile[key]
        #if the value is in the key, do one of the following:
        elif match_side in tile[key]:
            
            if match_side == tile[key][0]:
                tile[key] = rotate_right(tile[key])
                if tile[key][1] == match_side:
                    return key, tile[key]
                else:
                    raise ValueError(f"something went wrong when rotating key & top was a match. \
                             key is: {key}, \nmatch side: {match_side}\n{tile[key]}")
            
            if match_side == tile[key][2]:
                tile[key] = rotate_right(rotate_right(rotate_right(flip_vertical(tile[key]))))
                if tile[key][1] == match_side:
                    return key, tile[key]
                else:
                    raise ValueError(f"something went wrong when rotating key & bottom was a match. \
                             key is: {key}, \nmatch side: {match_side}\n{tile[key]}")
            
            if match_side == tile[key][3]:
                tile[key] = flip_vertical(tile[key])
                if tile[key][1] == match_side:
                    return key, tile[key]
                else:
                    raise ValueError(f"something went wrong when flipping key & left side was a match. \
                             key is: {key}, \nmatch side: {match_side}\n{tile[key]}")
        #if the value is in the key reversed, do one of the following:
        elif match_side[::-1] in tile[key]:
            
            if match_side[::-1] == tile[key][1]:
                tile[key] = flip_horizontal(tile[key])
                if tile[key][1] == match_side:
                    return key, tile[key]
                else:
                    raise ValueError(f"something went wrong when flipping key & right side was an inverse \
                             match.  key is: {key}, \nmatch side: {match_side}\n{tile[key]}")
            
            if match_side[::-1] == tile[key][0]:
                tile[key] = rotate_right(flip_vertical(tile[key]))
                if tile[key][1] == match_side:
                    return key, tile[key]
                else:
                    raise ValueError(f"something went wrong when rotating/flipping key & top side was an \
                             inverse match.  key is: {key}, \nmatch side: {match_side}\n{tile[key]}")

            if match_side[::-1] == tile[key][2]:
                tile[key] = rotate_right(rotate_right(rotate_right(tile[key])))
                if tile[key][1] == match_side:
                    return key, tile[key]
                else:
                    raise ValueError(f"something went wrong when rotating/flipping key & bottom was an \
                             inverse match.  key is: {key}, \nmatch side: {match_side}\n{tile[key]}")

            if match_side[::-1] == tile[key][3]:
                tile[key] = flip_vertical(flip_horizontal(tile[key]))
                if tile[key][1] == match_side:
                    return key, tile[key]
                else:
                    raise ValueError(f"something went wrong when rotating/flipping key & left was an \
                             inverse match.  key is: {key}, \nmatch side: {match_side}\n{tile[key]}")
    raise ValueError(f'did not find a match. match_side is {match_side}')
 
#returns the next match key where the next tile's top matches the bottom of the previous key.
def top_match(match_side: str, tile: Dict[int,List[str]]) -> Tuple[int,List[str]]:
    for key in tile.keys():
        #if it's a perfect match, return it.
        if match_side == tile[key][0]:
            return key, tile[key]
        #if the value is in the key, do one of the following:
        elif match_side in tile[key]:
            #if match is the right side:
            if match_side == tile[key][1]:
                tile[key] = rotate_right(rotate_right(rotate_right(tile[key])))
                if tile[key][0] == match_side:
                    return key, tile[key]
                else:
                    raise ValueError(f"something went wrong when rotating key to match top & right \
                             was a match. key is: {key}, \nmatch side: {match_side}\n{tile[key]}")
            #if the value matches bottom:
            if match_side == tile[key][2]:
                tile[key] = flip_horizontal(tile[key])
                if tile[key][0] == match_side:
                    return key, tile[key]
                else:
                    raise ValueError(f"something went wrong when rotating key to match top & bottom \
                             was a match. key is: {key}, \nmatch side: {match_side}\n{tile[key]}")
            #if the match is the left side.
            if match_side == tile[key][3]:
                tile[key] = rotate_right(flip_horizontal(tile[key]))
                if tile[key][0] == match_side:
                    return key, tile[key]
                else:
                    raise ValueError(f"something went wrong when flipping key to match top & left side \
                             was a match.  key is: {key}, \nmatch side: {match_side}\n{tile[key]}")
        #if the value is in the key reversed, do one of the following:
        elif match_side[::-1] in tile[key]:
            
            if match_side[::-1] == tile[key][0]:
                tile[key] = flip_vertical(tile[key])
                if tile[key][0] == match_side:
                    return key, tile[key]
                else:
                    raise ValueError(f"something went wrong when flipping key to match top & top side \
                             was an inverse match.  key is: {key}, \nmatch side: {match_side}\n{tile[key]}")
            #match is right & reversed.
            if match_side[::-1] == tile[key][1]:
                tile[key] = rotate_right(flip_vertical(tile[key]))
                if tile[key][0] == match_side:
                    return key, tile[key]
                else:
                    raise ValueError(f"something went wrong when rotating/flipping key to match top & \
                             right side was an inverse match.  key is: {key}, \nmatch side: {match_side}\n{tile[key]}")
            #match is bottom and reversed.
            if match_side[::-1] == tile[key][2]:
                tile[key] = flip_horizontal(flip_vertical(tile[key]))
                if tile[key][0] == match_side:
                    return key, tile[key]
                else:
                    raise ValueError(f"something went wrong when teselating key to match top & bottom \
                             was an inverse match.  key is: {key}, \nmatch side: {match_side}\n{tile[key]}")
            #match is left and reverse
            if match_side[::-1] == tile[key][3]:
                tile[key] = rotate_right(tile[key])
                if tile[key][0] == match_side:
                    return key, tile[key]
                else:
                    raise ValueError(f"something went wrong when teselating key to match top & left was \
                             an inverse match.  key is: {key}, \nmatch side: {match_side}\n{tile[key]}")
    raise ValueError(f'did not find a match. match_side is {match_side}')
 
def print_sea(tile_order:List[int],tile:Dict[int,List[str]],picture_size:int) -> str:
    ocean = ''
    #for tiles:
    for i in range(picture_size):
        #cells
        for j in range(8):
            for k in range(picture_size):
                ocean += tile[tile_order[i*picture_size+k]][4][j*8:j*8+8]
    for i in range(0,len(ocean),picture_size*8):
        print(ocean[i:i+picture_size*8])
    return ocean

def search_sea_horizontal(ocean:str,picture_size:int) -> int:
    search_area = []
    s = 0
    # chunks of 20 x 3
    #.........................O
    #O....OO....OO....OOO
    #.O..O..O..O..O..O
    sea_creature_1 = [(0,18),(1,0),(1,5),(1,6),(1,11),(1,12),(1,17),
                                (1,18),(1,19),(2,1),(2,4),(2,7),(2,10),(2,13),(2,16)]
    sea_creature_2 = [(0,1),(1,0),(1,1),(1,2),(1,7),(1,8),(1,13),(1,14),
                                (1,19),(2,18),(2,15),(2,12),(2,9),(2,6),(2,3)]
    sea_creature_1_count = 0
    sea_creature_2_count = 0
    total_creatures = 0
    #OR
    #
    #.O
    #OOO....OO....OO....O
    #      O..O..O..O..O..O
    row,col = 0,0
    check,checkid = "",[]
    #i = row*picture_size +col
    #picture is picture_size*8 x picture_size*8 in size.
    # to check section, as long as row and col isn't going to run over, grab that square.
    for row in range(picture_size*8-3):
        for col in range(picture_size*8-20):
            for i in range(row,row+3):
                for j in range(col,col+20):
                    if ocean[i*picture_size*8+j] =="#":
                        search_area.append((i-row,j-col))
                    check += ocean[i*picture_size*8+j]
                    checkid.append(i*picture_size*8+j)
                #checkid.append((i,j))
                check +="\n"
            '''if i == 4 and j == 22:
                print(f'i:{i},j:{j}')
                print(f'check string:\n {check},\n{checkid}\nlen:{len(check)},count:{check.count("#")},\
                       entries in search:\n{search_area}\n')'''
            #print(search_area)
            for creature in sea_creature_1:
                if creature in search_area:
                    sea_creature_1_count += 1
                if sea_creature_1_count == len(sea_creature_1):
                    total_creatures += 1

            for creature in sea_creature_2:
                if creature in search_area:
                    sea_creature_2_count += 1
                if sea_creature_2_count == len(sea_creature_2):
                    total_creatures += 1

            search_area, check, checkid, sea_creature_1_count, sea_creature_2_count=[],"",[],0,0
            
    return total_creatures

def rotate_ocean(ocean:str,picture_size:int) -> str:
    new_body = ""
    for i in range(0,picture_size*8):
        for j in range(1,picture_size*8+1):
            new_body += ocean[8*picture_size*(picture_size*8-j)+i]
        #print(f'i:{i},j:{j}')
        #print(f'new body:\n{new_body}')
    '''for i in range(0,len(ocean),picture_size*8):
            print(new_body[i:i+picture_size*8])'''
    return new_body

def main() -> int:
    tile = parse_it()
    total_edges = {}
    edge_tiles={}
    ans1 = 1
    for keys in tile.keys():
        side_match_total, edges = match(keys,tile)
        total_edges[keys] = edges
        if side_match_total < 3:
            print(f'Side found. {keys} has {side_match_total} total matches.')
            ans1 *= keys
            edge_tiles[keys]=edges
    #print(f'ans1: {ans1}')
 
    #time to put it all together.
    #tiles are saved as a list of: [0] = top, [1] = right, [2] = bottom, [3] = left, [4] = body
    #arbitrarily chose an edge to start.
    left_corner = 2551
    left_corner = 1951
    #Time to rotate left corner tile.
    #print(f'edge tiles: {edge_tiles[left_corner]}')

    i = 0
    while True:
        #check tile. top and left need to line up with the edges. can be forward or reversed...
        #top:
        if tile[left_corner][0] in [edge_tiles[left_corner][0], edge_tiles[left_corner][0][::-1] , edge_tiles[left_corner][1] , edge_tiles[left_corner][1][::-1]]:
            if tile[left_corner][3] in [edge_tiles[left_corner][1], edge_tiles[left_corner][1][::-1], edge_tiles[left_corner][0], edge_tiles[left_corner][0][::-1]]:
                break
            else:
                #print("almost there.")
                tile[left_corner] = flip_vertical(tile[left_corner])
        else:
            tile[left_corner] = rotate_right(tile[left_corner])
            #print(f' rotated left. top is now: {tile[left_corner][0]}')
        i += 1
        if i > 4:
            print('no solution found')
            break

    #print(f'{left_corner}: {tile[left_corner]}, {edge_tiles[left_corner]}')

    #Now we need to assemble tiles. Assume this is a square picture.
    picture_size = int(pow(len(tile),0.5))
    remaining_tiles = deepcopy(tile)
    
    tile_order:List[int] = [left_corner]
    match_tile = left_corner
    del remaining_tiles[match_tile]
    for i in range(picture_size):
        for j in range(1,picture_size):
            match_side = tile[match_tile][1] #right side. needs to match a left side.
            match_tile, match_stuff = right_match(match_side,remaining_tiles)
            #print(f'side match: {match_tile},\n{match_stuff[0:4]}\n{tile[match_tile][0:4]}')
            tile[match_tile] = flip_vertical(match_stuff)
            del remaining_tiles[match_tile]
            
            tile_order.append(match_tile)
        if i == (picture_size-1):
            pass
        else:
            match_side = tile[tile_order[i*picture_size]][2]#bottom, first tile in row. need to match a top.
            #print(f'match side: {match_side}')
            match_tile, match_stuff = top_match(match_side, remaining_tiles)
            tile[match_tile] = match_stuff
            #print(f'bottom match: {match_tile}')
            del remaining_tiles[match_tile]
            tile_order.append(match_tile)

    ocean = print_sea(tile_order,tile,picture_size)
    ans2 = 0
    ans2+= search_sea_horizontal(ocean,picture_size)
    print(ans2)
    for i in range(0,3):
        ocean = rotate_ocean(ocean,picture_size)
        ans2+= search_sea_horizontal(ocean,picture_size)
        print(i,ans2,(ocean.count("#") - ans2*15))
    
    return 0
    
if __name__ =='__main__':
    sys.exit(main())