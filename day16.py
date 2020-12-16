import sys, itertools, re
from copy import deepcopy

from typing import Dict, List, Optional, Set, Tuple, Union

def parse_it(input:List[str]) -> Tuple[List[str], List[List[List[int]]], List[int], List[List[int]]]:

    your_ticket: List [int] = []
    search_fields: List [str] = []
    search_ranges: List[ List [ List [int] ] ] = []
    nearby_tickets: List[ List[int] ] = []

    nearby_ticket_switch = 0

    for i in range(len(input)):
        if "your ticket:" in input[i-1]:
            your_ticket = [int(c) for c in input[i].split(',')]

        elif "nearby tickets" in input[i]:
            nearby_ticket_switch = 1

        elif nearby_ticket_switch == 1:
            nearby_tickets.append([int(c) for c in input[i].split(',')])

        elif ":" in input[i] and "your ticket" not in input[i]:
            field, raw_ranges = input[i].split(':')
            ranges = raw_ranges.strip().split(' or ')
            
            search_field_ranges = []

            for r in ranges:
                range_list = [int(c) for c in r.strip().split('-') ]
                search_field_ranges.append(range_list)
            search_fields.append(field)
            search_ranges.append(search_field_ranges)
            
        else:
            print(f"could not match line: {input[i]}")

    return search_fields, search_ranges, your_ticket, nearby_tickets

def good_and_evil(nearby_tickets: List[List[int]], search_ranges:List[List[List[int]]]) -> Tuple[List[int],List[List[int]]]:

    #check tickets:
    bad_ticket_number =[]
    good_tickets = []
    for ticket in nearby_tickets:
        if len(ticket) != len(search_ranges):
            raise ValueError("bad ticket length")

 
        #collect the values that are good in a ticket.
        good_ticket_value = 0

        for value in ticket:
            this_ticket_value = 0
            for ranges in search_ranges:
                #if the ticket is good, add to good_ticket_value.
                if (value in range(ranges[0][0],ranges[0][1]+1)) or (value in range(ranges[1][0],ranges[1][1]+1)):
                        this_ticket_value += 1
             #if it wasn't in any list, then it's bad.
            if this_ticket_value == 0:
                bad_ticket_number.append(value)
            else:
                good_ticket_value += 1

        #if all values were good in a ticket:
        if good_ticket_value == len(search_ranges):
                good_tickets.append(ticket)

    return bad_ticket_number, good_tickets

def sodoku(good_tickets: List[List[int]], search_fields: List[str], search_ranges:List[List[List[int]]]) -> List[List[str]]:
    return_list = [deepcopy(search_fields) for i in range( len( search_fields ) )]

    #print(return_list)

    for ticket in good_tickets:
        for value in ticket:
            for search in search_ranges:
                if (value not in range(search[0][0],search[0][1]+1)) and (value not in range(search[1][0],search[1][1]+1)):
                    #print(ticket.inde x(value),search_ranges.index(search),search_fields)
                    return_list[ticket.index(value)].remove(search_fields[search_ranges.index(search)])
                    #print(return_list)
    total_return_possibilities = sum([len(possible) for possible in return_list])

    while total_return_possibilities > 20:
        total_return_possibilities = sum([len(possible) for possible in return_list])
        for list in return_list:
            if len(list) == 0:
                raise ValueError(f"entry in return list is 0. {return_list}")
            if len(list) == 1:
                for i in range( len( return_list ) ) :
                    if i == return_list.index(list):
                        pass
                    elif list[0] in return_list[i]:
                        return_list[i].remove(list[0])
                        #print(return_list)
        if total_return_possibilities == sum([len(possible) for possible in return_list]):
            break
    return_list = [c[0] for c in return_list]
    print(return_list)
    return return_list

def main(args: List[str]) -> int:

    with open(args[1], 'r') as f:
        input = [ line.strip() for line in f ]

    search_fields, search_ranges, your_ticket, nearby_tickets = parse_it(input)

    bad_ticket_number,good_tickets = good_and_evil(nearby_tickets, search_ranges)

    #range order:
    return_list = sodoku(good_tickets,search_fields, search_ranges)
    ans2 = 1
    
    print(f"{search_fields}\n{your_ticket}")
    
    for item in return_list:
        if "departure" in item:
            print(f"{item}, {return_list.index(item)}")
            ans2 *=your_ticket[return_list.index(item)]

    print(sum(bad_ticket_number), ans2 )

    return 0

if __name__ == '__main__':
    sys.exit( main( sys.argv ) )