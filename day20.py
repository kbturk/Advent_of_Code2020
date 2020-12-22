#Tessellate matching game

import sys, re
from typing import Sequence, Optional, Dict, Pattern, Tuple, List

def flip_vertical(tile_stuff:List[str]) -> List[str]:
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
    for i in range(0,8):
        new_body += body[56-(i*8+8):56-i*8]
        print(new_body[i*8:i*8+8])
    print()
    #0 ,  1   ,    2     ,3   ,   4
    top,right,bottom,left,body = tile_stuff[2],tile_stuff[1][::-1],tile_stuff[0],tile_stuff[3][::-1],new_body
    print(f'{top}\n{right}\n{bottom}\n{left}')
    return [top,right,bottom,left,body]

def flip_horizontal(tile_stuff:List[str]) -> List[str]:
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
    #0 ,  1   ,    2     ,3   ,   4
    top,right,bottom,left,body = tile_stuff[0][::-1],tile_stuff[3],tile_stuff[2][::-1],tile_stuff[1],new_body
    #print(f'{top}\n{right}\n{bottom}\n{left}')
    return [top,right,bottom,left,body]

def rotate_left(tile_stuff:List[str]) -> List[str]:
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
        new_body += body[8*7+i]+body[8*6+i]+body[8*5+i]+body[8*4+i]+body[8*3+i]+body[8*2+i]+body[8+i]+body[0+i]
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
    print(f'Number of matches found: {matches_found}, sides not matched: {not_matched}')
    return matches_found, not_matched

def parse_it() -> Dict[int,List[str]]:

def main() -> int:
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
            body = body[11:19]+body[21:29]+body[31:39]+body[41:49]+body[51:59]+body[61:69]+body[71:79]+body[81:89]
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
            
    flip_vertical(tile[3079])

    ans1 = 1
    for keys in tile.keys():
        side_match_total, edges = match(keys,tile)
        tile[keys].append([edges])
        if side_match_total < 3:
            print(f'Side found. {keys} has {side_match_total}')
            ans1 *= keys
    print(f'ans1: {ans1}')
    return 0
    
if __name__ =='__main__':
    sys.exit(main())