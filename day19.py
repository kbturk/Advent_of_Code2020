#Conway game of life!

import sys, itertools, re
from typing import NamedTuple, Sequence, Optional, Pattern, Dict
from typing_extensions import Protocol

class Rule(Protocol):
    def compile(self, rules: 'Dict[int, Rule]') -> str:
        ...

class Lit(NamedTuple):
    lit: str

    def compile(self, rules: Dict[int, Rule]) -> str:
        return self.lit

class Ref(NamedTuple):
    location: int

    def compile(self, rules: Dict[int, Rule]) -> str:
        return rules[self.location].compile(rules)

class Chain(NamedTuple):
    rules: Sequence[Rule]

    def compile(self, rules: Dict[int, Rule]) -> str:
        return ''.join(r.compile(rules) for r in self.rules)

class Alt(NamedTuple):
    rules: Sequence[Rule]

    def compile(self, rules: Dict[int, Rule]) -> str:
        return '(' + '|'.join(r.compile(rules) for r in self.rules) + ')'

def main() -> int:
    rules: Dict[int, Rule] = dict()
    the_re: Optional[Pattern[str]] = None
    forty_two: Optional[Pattern[str]] = None
    thirty_one: Optional[Pattern[str]] = None
    valid,part2, done = 0,0, False

    for line in sys.stdin:
        line = line.rstrip()
        if ":" in line:

            location, rule = line.rstrip().split(':')
            alts = rule.split('|')
            altered = list()

            for a in alts:
                chain = a.split()
                chained = list()

                for c in chain:
                    base: Rule

                    if '"' in c:
                        base = Lit(c[1:-1])

                    else:
                        base = Ref(int(c))
                    chained.append(base)
                altered.append(Chain(chained))

            if len(altered) == 1:

                if len(altered[0].rules) ==1:
                    rules[int(location)] = altered[0].rules[0]

                else:
                    rules[int(location)] = altered[0]

            else:
                rules[int(location)] = Alt(altered)
        elif line == "":
            the_re = re.compile(rules[0].compile(rules))
            forty_two = re.compile(rules[42].compile(rules))
            thirty_one = re.compile(rules[31].compile(rules))
            print(the_re)
            done = True
            pass
        elif done:
            assert the_re is not None
            #total the matching lines
            if the_re.fullmatch(line):
            
                valid +=1
            #part 2. 42 and 31 can be repeated in a pattern, but there must be at least one more 42 than 31.
            assert forty_two is not None 
            assert thirty_one is not None
            n_42 = 0
            n_31 = 0
 
            while True:
                m = forty_two.match(line)
                if m:
                    #move to the end of the match and match again.
                    n_42 +=1
                    line = line[m.end(0):]
                else:
                    break
 
            #count 31's
            while True:
                    m = thirty_one.match(line)
                    if m:
                        #move to the end of the match and match again.
                        n_31 += 1
                        line = line[m.end(0):]
                    else:
                        break
             #count 42's
 
            if n_31 >= 1 and n_42 >= n_31 + 1 and line == "":
                part2 += 1

    print(valid)
    print(part2)
    
    return 0

if __name__ == '__main__':
    sys.exit( main( ) )