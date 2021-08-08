import os

if __name__ == "__main__":
    filepath = os.path.join(os.path.dirname(__file__), "../input.txt")

    answers = [0]*26
    groups_sums = 0
    with open(filepath) as f:
        for line in f.readlines():
            if line == "\n" and answers != []:
                groups_sums += answers.count(1)
                answers = [0]*26
            else:
                for c in line:
                    if c != '\n':   
                        pos = ord(c) - 97
                        answers[pos] = 1
    groups_sums += answers.count(1)
    print("Group Sums: ", groups_sums)