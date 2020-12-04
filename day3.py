import sys, argparse, random

def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('input file', help ='please provide an input file containing a list of ints.', type=str)
    return parser

def parse_it(str):
    parsed = []
    for letter in str:
        if letter == '.':
            letter = 0
        elif letter =='#':
            letter = 1
        parsed.append(letter)
    return parsed

#How many trees will you hit on your trajectory?
def oh_god_make_it_stop( i, j, l ):
    dings = 0

    position = [0,0]
    while position[1] < len( l ):
        dings += int( l[ position[1] ][0][ position[0] ] )
        position = [ (position[0] + i) % len( l[0][0] ), position[1] + j ]
    print(f"{random.choice(['ouch!','fuck','noooooo'])} x {dings}")
    return dings

def main( argv ):
    arg = arg_parser().parse_args( argv[1:] )

    with open( argv[1], 'r' ) as f:
        l = [ (parse_it( i.strip( '\n' )), j ) for j, i in enumerate( f ) ]

    #part1:
    print('part 1:')
    oh_god_make_it_stop(3,1,l)

    #part2:
    total = 1
    for entry in [(1,1),(3,1),(5,1),(7,1),(1,2)]:
        total = total*oh_god_make_it_stop(entry[0],entry[1],l)

    print(total)

if __name__ == '__main__':
    sys.exit( main( sys.argv ) )