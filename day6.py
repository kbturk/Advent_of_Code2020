import sys, re

def main(args):
    #part 1. Not that pretty...
    with open(args[1], 'r') as f:
        key = 0
        d = {}
        d.setdefault(key,[])
        for line in f:
            if line == '\n':
                key += 1
                d[key] = []
            else:
                for l in line.strip():
                    if l not in d[key]:
                        d[key].append(l)
    print(key, sum([len(value) for value in d.values()]))
    #part 2.
    with open(args[1],'r') as f:
        key = 0
        d = {}
        d.setdefault(key,[])
        a = 1
        for line in f:
            if line == '\n':
                a = 0
                key += 1
                d[key] = []
            else:
                l = [char for char in line.strip()]
                if a == 1:
                    d[key] = l
                    #print(f'new row: {key}: {l}, a: {a}')
                else:
                    
                    d2 = []
                    for v in d[key]:
                        if v in l:
                            d2.append(v)
                           # print(f"added '{v}'. list is now: {d2}, a:{a}")
                    d[key] = d2
                #print(d[key])
            a +=1
    #print(d)
    print(sum([len(value) for value in d.values()]))
if __name__ == '__main__':
    sys.exit( main( sys.argv ) )