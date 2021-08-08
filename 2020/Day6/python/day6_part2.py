import os

if __name__ == "__main__":
    filepath = os.path.join(os.path.dirname(__file__), "../input.txt")

    answers = [0]*26
    groups_sums = 0
    people_in_group = 0
    with open(filepath) as f:
        for line in f.readlines():
            if line == "\n" and answers != []:
                groups_sums += answers.count(people_in_group)
                people_in_group = 0
                answers = [0]*26
            else:
                people_in_group = people_in_group + 1
                for c in line:
                    if c != '\n':   
                        pos = ord(c) - 97
                        answers[pos] += 1
    groups_sums += answers.count(people_in_group)
    print("Group Sums: ", groups_sums)