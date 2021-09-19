import os
from sys import int_info

def read_input(filename):
    return open(filename).readlines()


def is_broken_loop(lines):
    seen_instruction = { x:0  for x in range(0,len(lines)) }
    acc = 0
    ip = 0
    run = True
    inf_loop = False
    while run:
        if ip >= len(lines):
            run = False
            inf_loop = False
            break

        line = lines[ip]
        cmd = line.split(" ")[0]
        value = line.split(" ")[1]

        seen_instruction[ip] += 1

        if seen_instruction[ip] > 1:
            print("infinite loop condition")
            print(f"on instruction n°{ip}.")
            inf_loop = True
            run = False

        if cmd == "acc":
            acc += int(value)
            ip += 1
        elif cmd == "jmp":
            ip += int(value)
        else:
            # nop case
            ip += 1
        
    if not inf_loop:
        print(f"acc = {acc}")

    return inf_loop


if __name__ == "__main__":
    filepath = os.path.join(os.path.dirname(__file__), "../input.txt")
    lines = read_input(filepath)

    nop_and_jmp = []
    acc = 0
    ip = 0
    run = True
    for i, line in enumerate(lines):
        cmd = line.split(" ")[0]
        value = line.split(" ")[1]

        if cmd in ("nop", "jmp"):
            nop_and_jmp.append(i)
    
    print(nop_and_jmp)
    for ins in nop_and_jmp:
        lines_copy = list(lines)
        if "nop" in lines_copy[ins]:
            lines_copy[ins] = lines_copy[ins].replace("nop", "jmp")
        else:
            lines_copy[ins] = lines_copy[ins].replace("jmp", "nop")
        
        print("~~~")
        print(f"Testing instruction #{ins}")
        if not is_broken_loop(lines_copy):
            print(f"The culprit was instruction #{ins}")
            break
