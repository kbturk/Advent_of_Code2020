import sys, argparse, random, re

def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('input file', help ='please provide an input file containing a list of ints.', type=str)
    return parser

def parse_it(arg):
    l = []
    with open( arg, 'r' ) as f:
        for line in f:
            line = line.strip('\n').translate(str.maketrans('FBLR','0101'))
            l.append((int(line[0:7],2)*8 + int(line[7:],2)))
    return l
        
def main( argv ):
    arg = arg_parser().parse_args( argv[1:] )
    ans = parse_it(argv[1])
    #part1:
    print(max(ans))
    #part2:
    for i in range(len(ans)-1):
        if sorted(ans)[i+1] - sorted(ans)[i] > 1:
            print(sorted(ans)[i+1],sorted(ans)[i])
    
if __name__ == '__main__':
    sys.exit( main( sys.argv ) )