import sys, argparse, re

def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('input file', help ='please provide an input file containing a list of ints.', type=str)
    return parser
def main( argv ):

    tot_part1, tot_part2 = 0, 0
    arg = arg_parser().parse_args(argv[1:])
    with open( argv[1], 'r' ) as f:
        for line in f:
            n = re.match(r'(?P<min_count>\w*)-(?P<max_count>\w*) (?P<letter>\w): (?P<existing_pw>\w*)', line)

            #make things a little easier to read...
            min_count = int(n.group('min_count')) #will just keep referring to this as min/max even though they're used as position arguments in the second part.
            max_count = int(n.group('max_count'))
            letter = n.group('letter')
            existing_pw = n.group('existing_pw')

            #part 1:
            if min_count <= existing_pw.count( letter ) <= max_count :
                #print(f" {n.group('letter')} found in {n.group('existing_pw')}" )
                tot_part1 = tot_part1 + 1

            #part 2:
            if (existing_pw[min_count-1] == letter or existing_pw[max_count-1] == letter) and (existing_pw[min_count-1] != existing_pw[max_count-1]) :
                tot_part2 = tot_part2 + 1

    print(f'{tot_part1}, {tot_part2}')

        
if __name__ == '__main__':
    sys.exit( main( sys.argv ) )