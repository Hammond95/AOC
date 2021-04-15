import os

def read_input(filename):
    return open(filename).readlines()

def get_sum_pair(elements, search, pos_map) -> tuple:
    num1 = None
    for element in elements:
        num2 = search - element
        if pos_map.get(num2):
            num1 = element
            break
    
    return num1, num2

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('search', metavar='search', type=int, help='The sum integer to find')
    args = parser.parse_args()

    input_lines = read_input(os.path.join(os.path.dirname(__file__),"../input.txt"))
    elements = [ int(x.strip()) for x in input_lines ]

    pos_map = dict(zip(elements, range(0, len(elements))))

    num3 = None
    for i, element in enumerate(elements):
        sub_search = args.search - element
        sub_elements = elements[:i] + elements[i+1:]
        sub_pos_map = pos_map.copy()
        _ = sub_pos_map.pop(element)

        num1, num2 = get_sum_pair(sub_elements, sub_search, sub_pos_map)
        if num1 and num2:
            num3 = element
            break
    
    if num3:
        print(f"Magic Numbers: {num1} + {num2} + {num3} = {num1+num2+num3}.")
        print(f"The solution is: {num1} x {num2} x {num3} = {num1*num2*num3}.")
    else:
        print("No valid tris found.")
