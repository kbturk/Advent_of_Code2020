import sys, itertools

def check_it(l):
    for i in range(26,len(l)):
        check = sorted(itertools.islice(l,i-26,i))

        if check[0]+check[1] <= l[i] <= check[len(check)-2]+check[len(check)-1]:
            small_check = [c[0]+c[1] for c in itertools.combinations(check,2)]
            if l[i] not in small_check:
                print(f'number issue found: on {i}, {l[i]} is not in list {small_check}')
                return l[i], i
        else:
            print(f'number issue found: on {i}, {l[i]} is not between {check[0]+check[1]} and {check[23]+check[24]}.\nlist used was:{check}')
            return l[i], i

def check_it_twice(l,l_i,i):
    n,m = 0,1
    while m < i:
        if sum(itertools.islice(l,n,m+1)) != l_i:
            if sum(itertools.islice(l,n,m+2)) == l_i:
                print(f'ans found: {sum(itertools.islice(l,n,m+2))} = {l_i}\n{list(itertools.islice(l,n,m+2))}')
                return
            while sum(itertools.islice(l,n,m+1)) < l_i:
                m +=1
            n +=1
        else:
            ans2 = sorted(list(itertools.islice(l,n,m+1)))[0]+sorted(list(itertools.islice(l,n,m+1)))[-1]
            print(f'ans found: {sum(itertools.islice(l,n,m+1))} = {l_i}\nans:{ans2}\n{list(itertools.islice(l,n,m+1))}')
            return

def main(args):

    with open(args[1], 'r') as f:
        l = [int(line.strip()) for line in f]
    #part 1
    l_i, i = check_it(l)
    #part 2
    check_it_twice(l,l_i,i)

if __name__ == '__main__':
    sys.exit( main( sys.argv ) )