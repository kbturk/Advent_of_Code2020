import sys, copy

def game_boy_go_burrrr(l):

    global_value = 0
    i = 0
    j = []

    while i not in j:
        instr, oper = l[i]
        j.append(i)

        if instr == 'nop':
            i += 1
        elif instr == 'jmp':
            i += int(oper)
        elif instr == 'acc':
            i += 1
            global_value += int(oper)
        else:
            print('error!')
            break
        if i == len(l):
            return True, global_value
    return False, global_value

def main(args):

    with open(args[1], 'r') as f:
        l = [line.strip().split(' ') for line in f]
    #part 1
    print(f'part 1 ans: {game_boy_go_burrrr(l)[1]}')
    #part 2
    for i in range(len(l)):
        l_copy = copy.deepcopy(l)

        if l_copy[i][0] == 'jmp':
            l_copy[i][0] = 'nop'

        elif l_copy[i][0] == 'nop':
            l_copy[i][0] = 'jmp'

        result, total = game_boy_go_burrrr(l_copy)

        if result:
            print(f'part 2 ans:{total}')
            break
    
if __name__ == '__main__':
    sys.exit( main( sys.argv ) )