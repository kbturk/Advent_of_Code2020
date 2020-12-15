import sys, itertools, re
from copy import deepcopy

from typing import Dict, List, Optional, Set, Tuple

def main(args: List[str]) -> int:

    registrar: Dict[int,int]= {}

    with open(args[1], 'r') as f:
        input = [ line.strip() for line in f ]
    for line in input:
        if "mask" in line:
            _,_, mask_input_string = line.split()
            print(mask_input_string)

            ones_mask = 0b000000000000000000000000000000000000
            zeros_mask = 0b111111111111111111111111111111111111

            for i,c in enumerate(mask_input_string):
                bit_pos = 35 - i
                if c == '1':
                    ones_mask = ones_mask | 1 << bit_pos
                elif c == '0':
                    zeros_mask = zeros_mask ^ 1 << bit_pos
        elif "mem" in line:
            #convert the line into a list of locations and registrars

            added_commands = re.fullmatch( r'mem\[([0-9]+)\] = ([0-9]+)', line )
            key, value = int(added_commands.group(1)), int(added_commands.group(2))
            value = value | ones_mask
            value = value & zeros_mask
            registrar[key] = value

    print(sum(registrar.values()))

    return 0

if __name__ == '__main__':
    sys.exit( main( sys.argv ) )