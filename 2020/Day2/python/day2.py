import os

def read_input(filename):
    return open(filename).readlines()


if __name__ == "__main__":
    lines = read_input(os.path.join(os.path.dirname(__file__),"../input.txt"))
    
    valid_psw_count = 0
    for line in lines:
        boundaries, password = line.split(":")
        min_val = int(boundaries.split(" ")[0].split("-")[0])
        max_val = int(boundaries.split(" ")[0].split("-")[1])
        letter = boundaries.split(" ")[1][0]

        password = password.strip()
        occurrences = password.count(letter)

        if min_val <= occurrences <= max_val:
            valid_psw_count = valid_psw_count + 1
    
    print(f"Valid Passwords Count: {valid_psw_count}.")
    