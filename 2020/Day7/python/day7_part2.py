import os
import re

def recursive_total(bags, color, excluded):
        tot = 0
        bag = bags.get(color)
        inner_bags = bag.keys()

        for inner_bag in inner_bags:
            if inner_bag in excluded:
                pass
            tot += (
                bags[color][inner_bag] * 
                (1 + recursive_total(bags, inner_bag, excluded))
            )

        return tot

if __name__ == "__main__":
    rgx = r"([a-z]+\s[a-z]+)\s(bags contain)\s(.*)"
    rgx2 = r"([0-9]+) ([a-z]+ [a-z]+) bag[s]?"

    filepath = os.path.join(os.path.dirname(__file__), "../input.txt")

    bags = {}
    with open(filepath) as f:
        for line in f.readlines():
            m = re.match(rgx, line)
            if m:
                color = m.group(1)
                child_bags = m.group(3)
                matches = re.findall(rgx2, child_bags)
                bags[color] = {}
                if matches != []:
                    for match in matches:
                        bags[color][match[1]] = int(match[0])
    
    print("Bag Colors that require less than 10 bags")
    print("--------------------------------------------")
    lt10 = []
    for color in bags.keys():
        tot = recursive_total(bags, color, [])
        if 0 < tot < 10:
            lt10.append((color, tot))
    lt10 = sorted(lt10, key=lambda x: x[1], reverse=True)

    row_format ="{:20}{:5}"
    print(row_format.format("bag color", "   tot"))
    print("===============================")
    for bag in lt10:
        print(row_format.format(bag[0], bag[1]))

    print("\n\nShiny Gold solution:")
    print("    shiny gold    ", recursive_total(bags, "shiny gold", []))
