import os

def read_input(filename):
    return open(filename).readlines()

def get_sum_pair(elements, search) -> tuple:
    posMap = dict(zip(elements, range(0, len(elements))))

    num1 = None
    for element in elements:
        num2 = search - element
        if posMap.get(num2):
            num1 = element
            break
    
    return num1, num2

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('search', metavar='search', type=int, help='The sum integer to find')
    args = parser.parse_args()

    input_lines = read_input(os.path.join(os.path.dirname(__file__),"../input.txt"))
    casted = [ int(x.strip()) for x in input_lines ]

    num1, num2 = get_sum_pair(casted, args.search)

    if num1 and num2:
        print(f"Magic Numbers: {num1} + {num2} = {num1+num2}.")
        print(f"The solution is: {num1} x {num2} = {num1*num2}.")
    else:
        print("No valid pair found.")
