#Conway game of life!

import sys, itertools, re
from typing import Optional, Tuple

def nat(inp: str) -> Optional[Tuple[str,int]]:
    digits = []
    while inp and inp[0].isdigit():
        digits.append(inp[0])
        inp = inp[1:]
    if not digits:
        return None
    return inp, int("".join(digits))

def term(inp:str) -> Optional[Tuple[str,int]]:
    res = nat(inp)
    #print(f'term res: {res}')
    if res is not None:
        return res

    if not inp or inp[0] != '(':
        return None
    res = expr( inp[1:] )
    if res is None:
        return None
    inp, ex = res
    if not inp or inp[0] !=')':
        return None
    return inp[1:], ex

def factor(inp:str) -> Optional[Tuple[str,int]]:
    res = term(inp)
    #print(f'factor res: {res}')
    if res is None:
        return None
    rest, t = res
    while True:
        res = add_term(rest)
        if res is not None:
            rest, add_t = res
            t += add_t
        else:
            break
    #print(f'returning factor res: {rest}')
    return rest, t

def add_term(inp:str) -> Optional[Tuple[str,int]]:
    if not inp or inp[0] != '+':
        return None
    return term(inp[1:])

def mul_term(inp:str) -> Optional[Tuple[str,int]]:
    if not inp or inp[0] != '*':
        return None
    #print(f'mult term returning: {inp}')
    return factor(inp[1:])


def expr(inp:str) -> Optional[Tuple[str,int]]:
    res = factor(inp)
    #print(f'expr res: {res}')
    if res is None:
        return None
    rest, t = res
    while True:
        res = mul_term(rest)
        #print(f'expr res is now:{res}')
        if res is not None:
            rest, mul_t = res
            t *= mul_t
        else:
            break
    return rest, t

def main() -> int:
    total = 0
    for line in sys.stdin:
        stripped = ''.join(c for c in line if not c.isspace() )
        #print(stripped)
        res = expr(stripped)
        if res is None:
            print( f'Bad expression: {stripped}', file=sys.stderr )
            return 1
        rest, val = res
        if rest:
            print( f'extra input: {rest}', file=sys.stderr )
        total += val
    print(total)  
    return 0

if __name__ == '__main__':
    sys.exit( main( ) )