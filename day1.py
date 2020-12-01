import sys, argparse

def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('input file', help ='please provide an input file containing a list of ints.', type=str)
    return parser
def main( argv ):

    l = []
    arg = arg_parser().parse_args(argv[1:])
    with open( argv[1], 'r' ) as f:
        for line in f:
            l.append( int( line.strip( '\n' ) ) )
    #part one:
    for i in l:
        r = 2020-i
        if r in l:
            print( f'part one pair found: {i}, {r}, { i * r }' )
            break
    #part two:
    for i in l:
        r1 = 2020 - i
        for j in l:
            r2 = r1 - j
            if r2 in l:
                if i == j:
                    continue
                if j == r2:
                    continue
                print(f'part two answer found: { i, j, r2 }, { i * j * r2 }') 
                return
        
if __name__ == '__main__':
    sys.exit( main( sys.argv ) )