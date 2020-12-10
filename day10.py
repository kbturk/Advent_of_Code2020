import sys, itertools
from copy import deepcopy


def main(args):

    with open(args[1], 'r') as f:
        l = sorted([int(line.strip()) for line in f])
    mn, mx = 0, int(max(l)+3)

    diff = []
    #part1:
    my_list = deepcopy(l)
    my_list.insert(0,mn)
    my_list.append(mx)
    
    for i in range(len(my_list)-1):
        diff.append( int( my_list[i+1]-my_list[i] ) )
    print(f"1's: {diff.count(1)}, 3's: {diff.count(3)}, total: {diff.count(1)*diff.count(3)}")

     #part2:
    paths = { my_list[0]:1 }
    for x in my_list[1:]:
        paths[x] = sum(paths[x-y] for y in range(1,4) if x-y in paths)
    print(f'part 2: {paths[my_list[-1]]}')
     

if __name__ == '__main__':
    sys.exit( main( sys.argv ) )