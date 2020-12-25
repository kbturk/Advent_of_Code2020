import sys, re
from typing import Dict, List, Tuple, Set,Union

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
    if player_1[0] > player_2[0]:
        player_1.append(player_1[0])
        player_1.append(player_2[0])
    else:
        player_2.append(player_2[0])
        player_2.append(player_1[0])

    player_1.remove(player_1[0])
    player_2.remove(player_2[0])

    return player_1,player_2

def main() -> int:
    player_1, player_2 = deal_it()

    winner,ans1 = [],0

    while (len(player_1) > 0) and (len(player_2) > 0):
        player_1, player_2 = play_it(player_1,player_2)
        if len(player_1) == 0:
            winner = player_2
        if len(player_2) == 0:
            winner = player_1
    print(f'player_1: {player_1}\nplayer_2: {player_2}')

    for i in range(len(winner)):
        ans1 += winner[i]*(len(winner)-i)
    print(ans1)
    return 0

if __name__ == '__main__':
    sys.exit(main())