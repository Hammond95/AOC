import os
import re


def recursive_count(rules, colors, excluded):
        tot = 0
        for color in colors:
            if color in excluded:
                pass
            parents = rules.get(color)
            if parents:
                tot += len(
                    [ p for p in parents if p not in excluded ]
                )
                excluded.extend(parents)
                tot += recursive_count(rules, parents, excluded)
        return tot

if __name__ == "__main__":
    rgx = r"([a-z]+\s[a-z]+)\s(bags contain)\s(.*)"
    rgx2 = r"([0-9]+) ([a-z]+ [a-z]+) bag([s]?)"

    filepath = os.path.join(os.path.dirname(__file__), "../input.txt")

    bags_parents = {}
    with open(filepath) as f:
        for line in f.readlines():
            m = re.match(rgx, line)
            if m:
                parent_color = m.group(1)
                child_bags = m.group(3)
                matches = re.findall(rgx2, child_bags)
                if matches != []:
                    for match in matches:
                        if bags_parents.get(match[1]):
                            bags_parents[match[1]].append(parent_color)
                        else:
                            bags_parents[match[1]] = [parent_color]
    
    print(
        recursive_count(bags_parents, ["shiny gold"], [])
    )

                    
