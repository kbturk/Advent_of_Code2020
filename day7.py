import sys, re

def parse_it(line: str):
    key, value = line.strip().split('contain')
    k1,k2,_,_ = key.split(' ')
    key_color = f'{k1} {k2}'

    value_description = []
    if 'no other bags' in value:
        return key_color,[]

    for v in value.split(','):
        _, x1, x2, x3, _ = v.split(' ')
        value_description.append((int(x1),f'{x2} {x3}'))

    return key_color, value_description

def main(args):
    #part 1. Not that pretty...
    d = {}
    with open(args[1], 'r') as f:
        for line in f:
            rule = parse_it(line)
            d[rule[0]] = rule[1]
    print(f"{d}")
    tot = 0
    for key in d:
        print(f'running with {key}, {d[key]}')
        res = master_count(key, d)
        if res == None:
            pass
        else:
            tot += 1
    print(tot)

def master_count(key,d):
    for (_,v) in d[key]:
        if v =='shiny gold':
            print(f'{key} contains: shiny gold. returning a 1')
            return 1
        elif v in d.keys():
            print(f'running master count again. old key was: {key}, new key is: {v},')
            if master_count(v,d) == 1:
                return 1
        else:
            return 0
if __name__ == '__main__':
    sys.exit( main( sys.argv ) )