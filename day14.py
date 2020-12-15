import sys, itertools, re
from copy import deepcopy

from typing import Dict, List, Optional, Set, Tuple

def floating_bit_poss(floating_mask: int, value:int) -> Set[int]:

    if floating_mask == 0:
        return {value}

    for i in range(36):
        bit_pos = 35 - i

        if floating_mask & (1 << bit_pos):
            value_hi = value | (1 << bit_pos)
            value_lo = value &~ (1 << bit_pos)
            return (floating_bit_poss(floating_mask &~ (1 << bit_pos),value_hi) |
             floating_bit_poss(floating_mask &~ (1 << bit_pos), value_lo))
    raise Exception("Reached impossible state.")
            
def main(args: List[str]) -> int:
    registrar: Dict[int,int]= {}

    with open(args[1], 'r') as f:
        input = [ line.strip() for line in f ]
    for line in input:
        if "mask" in line:
            _,_, mask_input_string = line.split()
            print(mask_input_string)

            ones_mask = 0b000000000000000000000000000000000000
            #no more zero masks...
            floating_mask = 0b000000000000000000000000000000000000
            
            for i,c in enumerate(mask_input_string):
                bit_pos = 35 - i
                if c == '1':
                    ones_mask |= ( 1 << bit_pos )
                elif c == 'X':
                    floating_mask |= ( 1 << bit_pos )

        elif "mem" in line:
            #convert the line into a list of locations and registrars
            added_commands = re.fullmatch( r'mem\[([0-9]+)\] = ([0-9]+)', line )
            key, value = int(added_commands.group(1)), int(added_commands.group(2))
            addr = key | ones_mask
            #now generate the remaining iterations:
            for key in floating_bit_poss(floating_mask, addr):
                registrar[key] = value
            #value = value & zeros_mask
            

    print(sum(registrar.values()))

    return 0

if __name__ == '__main__':
    sys.exit( main( sys.argv ) )