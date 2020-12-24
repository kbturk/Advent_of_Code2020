import sys, re
from typing import Dict, List, Tuple, Set,Union

def main() -> int:
    allergen_match: Dict[str,Set[str]] ={}
    total_ingredients: Dict[str,int] = {}
    for line in sys.stdin:
        switch = False
        ingredients: Set[str] = set()
        allergens: Set[str] = set()
        for c in line.strip().split():
            if "(contains" in c:
                switch = True
            elif ")" in c:
                    allergens.add(c.strip(")"))
            elif switch:
                allergens.add(c.strip(","))
            else:
                ingredients.add(c.strip())
        #last item in line. time to build the dictionary & ingredients list w count.
        for ingredient in ingredients:
            if ingredient in total_ingredients:
                total_ingredients[ingredient] +=1
            else:
                total_ingredients[ingredient] = 1
        for allergen in allergens:
            if allergen in allergen_match:
                allergen_match[allergen] = allergen_match[allergen].intersection(ingredients)
            else:
                allergen_match[allergen] = ingredients
    value = {a for c in allergen_match.values() for a in c}
    for v in value:
        if v in total_ingredients:
            del total_ingredients[v]

    print(f'part 1:{sum(total_ingredients.values())}')

    #part 2:
    i = 0
    while len([a for c in allergen_match.values() for a in c]) > len(allergen_match.keys()):
        for value in allergen_match.values():
            if len(value) == 1:
                for key in allergen_match.keys():
                    if allergen_match[key] == value:
                        pass
                    else:
                        allergen_match[key] = allergen_match[key].difference(value)
        i +=1
        if i ==20:
            break
    #print(f'allergen match: {allergen_match}')
    final_list = sorted(allergen_match.keys())
    #print(final_list)
    final_ingredient_list = []
    for item in final_list:
        final_ingredient_list.append(allergen_match[item])
    print(final_ingredient_list)
    
    return 0

if __name__ == '__main__':
    sys.exit(main())