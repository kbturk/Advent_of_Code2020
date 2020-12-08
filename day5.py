import sys, argparse, random, re

def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('input file', help ='please provide an input file containing a list of ints.', type=str)
    return parser

def main( argv ):
    arg = arg_parser().parse_args( argv[1:] )
    l = []
    with open(argv[1], 'r') as f:
        for line in f:
            if not re.fullmatch(r'((F|B){7})((L|R){3})',line.strip()):
                print('issue with input!')
                break
            l.append(int(line.strip('\n').translate(str.maketrans('FBLR','0101')),2))

    #part1:
    print(f'max: {max(ans)}')
    #part2:
    for i in range(len(ans)-1):
        if sorted(ans)[i+1] - sorted(ans)[i] > 1:
            print(sorted(ans)[i+1],sorted(ans)[i])
    
if __name__ == '__main__':
    sys.exit( main( sys.argv ) )