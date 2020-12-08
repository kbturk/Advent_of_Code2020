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


def master_count(key,d):
    for (_,v) in d[key]:
        if v =='shiny gold':
            return 1
        elif v in d.keys():
            if master_count(v,d) == 1:
                return 1
        else:
            return 0

def tot_bag_container(key,d):
    sum = 0
    #print(f'walking with: {key}, sum = {sum}')
    if d[key] == []:
        #print(f'end, {key}: {sum}')
        pass
    else:
        for (num, bag) in d[key]:
            sum += num + num * tot_bag_container(bag,d)
            #print(f'current total for {key} last ran {bag} with number {num}: {sum}')
    return sum

def main(args):
    #part 1.
    d = {}
    with open(args[1], 'r') as f:
        for line in f:
            rule = parse_it(line)
            d[rule[0]] = rule[1]
    #print(f"{d}")
    tot = 0
    for key in d:
        #print(f'running with {key}, {d[key]}')
        res = master_count(key, d)
        if res == None:
            pass
        else:
            tot += 1
    print(tot)
    print(tot_bag_container('shiny gold',d))

    
if __name__ == '__main__':
    sys.exit( main( sys.argv ) )