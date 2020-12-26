import sys, re
from typing import Dict, List, Tuple, Set,Union
from copy import deepcopy

def deal_it() -> Tuple[List[int],List[int]]:
    player_1= []
    player_2= []
    player = 1
    for line in sys.stdin:
        if line.strip() == "Player 1:":
            pass
        elif line.strip() == "Player 2:":
            player = 2
        elif line.strip() =="":
            pass
        elif player == 1:
            player_1.append(int(line.strip()))
        elif player == 2:
            player_2.append(int(line.strip()))
    return player_1,player_2

def play_it( player_1: List[int], player_2: List[int] ) -> Tuple[ List[ int ], List[ int ] ]:
    part = 2
    if part == 1:
        if player_1[0] > player_2[0]:
            player_1.append(player_1[0])
            player_1.append(player_2[0])
        else:
            player_2.append(player_2[0])
            player_2.append(player_1[0])

        player_1.remove(player_1[0])
        player_2.remove(player_2[0])

    if part == 2:
        p1_card = player_1[0]
        p2_card = player_2[0]
        
        player_1.remove(player_1[0])
        player_2.remove(player_2[0])
        #print(f'p1:{p1_card} ::{player_1}\np2:{p2_card} ::{player_2}')
        #print(f'{p1_card} >= {len(player_1)} {p1_card >= len(player_1)} or\
        #      {p2_card} > {len(player_2)} {p2_card > len(player_2)}')
             
        if ( p1_card > len(player_1) ) or ( p2_card > len(player_2) ):
            if p1_card > p2_card:
                player_1.append(p1_card)
                player_1.append(p2_card)
            else:
                player_2.append(p2_card)
                player_2.append(p1_card)
        #recursion time
        else:
            #print('recursion triggered.')
            seen_it:Dict[int,Tuple[int,int]] = {}
            round = 0
            player_1_copy = deepcopy(player_1[:p1_card])
            player_2_copy = deepcopy(player_2[:p2_card])
            winner = ""
            while(len(player_1_copy) > 0 ) and (len(player_2_copy) > 0):
                if (total_it(player_1_copy),total_it(player_2_copy)) in seen_it.values():
                    print('player 1 wins.')
                    winner ="p1"
                    break
                else:
                    seen_it[round] = (total_it(player_1_copy),total_it(player_2_copy))
                player_1_copy, player_2_copy = play_it(player_1_copy,player_2_copy)
                round +=1
                if len(player_1_copy) == 0:
                    winner = "p2"
                    break
                if len(player_2_copy) == 0:
                    winner = "p1"
                    break
            if winner == "p1":
                player_1.append(p1_card)
                player_1.append(p2_card)
            elif winner == "p2":
                player_2.append(p2_card)
                player_2.append(p1_card)
            else:
                raise ValueError("recursion issue. While loop did not return a winner.\np1:{player_1}\np2:{player_2}")
            #print("recursion exited.")
    return player_1,player_2

def total_it(winner: List[int]) -> int:
    total = 0
    for i in range(len(winner)):
        total += winner[i]*(len(winner)-i)

    return total

def main() -> int:
    player_1, player_2 = deal_it()
    #select part 1 or part 2:
    part = 2
    winner = []
    if part == 1:
        while (len(player_1) > 0) and (len(player_2) > 0):
            player_1, player_2 = play_it(player_1,player_2)
            if len(player_1) == 0:
                winner = player_2
            if len(player_2) == 0:
                winner = player_1
        print(f'player_1: {player_1}\nplayer_2: {player_2}')

        ans1 = total_it(winner)
        print(ans1)

    #part 2
    elif part == 2:
        seen_it:Dict[int,Tuple[int,int]] = {}
        ans2,round = 0,0
        print("part2")
        while (len(player_1) > 0) and (len(player_2) > 0):
            if (total_it(player_1),total_it(player_2)) in seen_it.values():
                print(f'player 1 wins')
                winner = player_1
                break
            else:
                seen_it[round] = (total_it(player_1),total_it(player_2))
                #print(f'seen it: {seen_it}')
            player_1, player_2 = play_it(player_1,player_2)

            round +=1
            if len(player_1) == 0:
                winner = player_2
                break
            if len(player_2) == 0:
                winner = player_1
                break
        print(f'player_1: {player_1}\nplayer_2: {player_2}')

        for i in range(len(winner)):
            ans2 += winner[i]*(len(winner)-i)
        print(ans2)
    else:
        raise ValueError("please set part to 1 or 2.")
    return 0

if __name__ == '__main__':
    sys.exit(main())