import sys, argparse, random, re

def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('input file', help ='please provide an input file containing a list of ints.', type=str)
    return parser

def parse_it( arg ):
    d, entry = {}, 0
    with open( arg, 'r' ) as f:
        for line in f:
            if line == '\n':
                entry += 1
            else:
                line = line.strip('\n').split()
                dict = {}
                for x in line:
                    i,j = x.split(':')
                    dict[i] = j
                if entry in d:
                    d[entry].update(dict)
                else:
                    d[entry] = dict
    return d

#good lord...
def check_it_good(e):
    
    #test 1:
    if not ((1920 <= int(e['byr']) <= 2002) and (2010 <= int(e['iyr']) <= 2020) and (2020 <= int(e['eyr']) <= 2030)):
        print(f"failed first test: {int(e['byr'])}, {int(e['iyr'])}, {int(e['eyr'])}")
        return 0 
    #test 2:
    x = re.findall(r'(?P<number>[0-9]+)in',e['hgt'])
    if (match := re.fullmatch(r'([0-9]+)(in|cm)',e['hgt'])) :
        if match.group(2) == 'in':
            if not ( 59 <= int(match.group(1)) <= 76 ) :
                print(f'failed 2nd test: {match}')
                return 0
        elif match.group(2) == 'cm':
            if not ( 150 <= int(match.group(1)) <= 193 ) :
                return 0
    else: 
        print(f"failed 2nd test: '{e['hgt']}'")
        return 0

    #test 3:
    if not re.fullmatch(r'#([0-9a-f]{6})',e['hcl']):
        print(f"failed 3rd test: {e['hcl']} {re.findall(r'#([0-9a-f]{6,6})',e['hcl'])}")
        return 0
    #test 4:
    if not re.fullmatch(r'(amb|blu|brn|gry|grn|hzl|oth)',e['ecl']):
        print(f"failed 4th test: {e['ecl']},{re.findall(r'(amb|blu|gry|grn|hzl|oth)',e['ecl'])}")
        return 0
    #test 5:
    if not re.fullmatch(r'[0-9]{9}',e['pid']):
        print(f"failed 5th test: {e['pid']}, {re.fullmatch(r'[0-9]{9}',e['pid'])}")
        return 0
    print(f'passed. {sorted(e.items(), key = lambda x: x)}')
    return 1
        
def main( argv ):
    arg = arg_parser().parse_args( argv[1:] )
    d = parse_it( argv[1] )

    #part1:
    ans1, ans2 = 0,0
    for e in iter(d.values()):
        if 'cid' in e:
            del e['cid']
        if len(e.values()) == 7:
            ans1 +=1
            #part2:
            ans2 += check_it_good(e)

    print(ans1, ans2)
if __name__ == '__main__':
    sys.exit( main( sys.argv ) )