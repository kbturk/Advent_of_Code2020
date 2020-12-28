import sys
from typing import Dict, List, Tuple, Set, Union
from copy import deepcopy

def find_loop_size(subject_number:int, value:int, public_key:int) -> int:
    loop_size = 0
    while value != public_key:
        value *=subject_number
        value %=20201227
        loop_size +=1
    return loop_size

def final_transformation(subject_number:int, value:int, loop_size:int) -> int:

    for i in range(loop_size):
        value *=subject_number
        value %=20201227
    return value

def main() -> int:
    #there are two loop sizes: one for the card, one for the door. This is a "secret" value.

    card_subject_number = 7
    value = 1
    card_public_key = 10212254

    card_loop_size = find_loop_size(card_subject_number,value,card_public_key)

    door_subject_number = 7
    value = 1
    door_public_key = 12577395

    door_loop_size = find_loop_size(door_subject_number,value,door_public_key)

    ans = final_transformation(door_public_key,value,card_loop_size)

    print(card_loop_size,door_loop_size,ans)

    
    return 0

if __name__ == "__main__":
    sys.exit(main())