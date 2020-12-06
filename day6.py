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
    print(sum([len(value) for value in d.values()]))
    #part 2. Could be merged into part one but I'm feeling lazy.
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
                l = sorted([char for char in line.strip()])
                if a == 1:
                    d[key] = l
                else:
                    d[key] = list(set(d[key]).intersection(set(l)))
            a +=1

    print(sum([len(value) for value in d.values()]))
if __name__ == '__main__':
    sys.exit( main( sys.argv ) )