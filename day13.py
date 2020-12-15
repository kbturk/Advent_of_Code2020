import sys, itertools
from copy import deepcopy

from typing import Dict, List, Optional, Set, Tuple

def timing(start_time:int,bus_time_list:List[int]) -> int:
    time = deepcopy(start_time)

    while True:
        for item in bus_time_list:
            if time%item == 0:
                return (time-start_time)*item
        time += 1
    print(f'no solution found.')

    return (time-start_time)*item

def timing2(start_time:int, departure_times: List[int], 
            bus_time_list: List[int]) -> Tuple[int,List[int]]:

    time = deepcopy(start_time)
    step, result = 1, 0
    for i in range(len(departure_times)):
        k, m = bus_time_list[i],departure_times[i]
        while result % k != m:
            result += step
        step *= k
    return result, step

def main(args: List[str]) -> int:

    with open(args[1], 'r') as f:
        input = [line.strip() for line in f ]

    timestamp = int(input[0])
    departure_times = list(enumerate(input[1].split(',')))
    departure_times = [a for a,b in departure_times if b != 'x']

    bus_time_list = [int(b) for b in input[1].split(',') if b != 'x']

    print(f'departure times: {departure_times}')
    print(f'          input: {bus_time_list}')

    #make the check list with the offset:
    true_departure_times = [0] #first element is 0

    for i in range(1,len(departure_times)):
        n = 1
        while n*bus_time_list[i] - departure_times[i] < 0:
            n += 1
        true_departure_times.append(n*bus_time_list[i]-departure_times[i])
    

    print(f'                 {true_departure_times}')
    print(timing(timestamp, bus_time_list))
    print(timing2(timestamp, true_departure_times, bus_time_list))

    return 0

if __name__ == '__main__':
    sys.exit( main( sys.argv ) )