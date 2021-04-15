import os

def read_input(filename):
    return open(filename).readlines()

def get_sum_pair(elements, search) -> tuple:
    size = len(elements)
    for i, element in enumerate(elements):
        print(f"#{i} {element}")
        paired = search - element
        pivot = size//2
        upper_bound = size-1
        lower_bound = i
        stay_in = True
        paired_pos = None
        while stay_in and (upper_bound-lower_bound > 1):
            if elements[pivot] == paired:
                stay_in = False
                paired_pos = (elements[i], elements[pivot])
            elif elements[pivot] < paired:
                lower_bound = pivot
                pivot = (pivot + upper_bound)//2
            else:
                upper_bound = pivot
                pivot = (lower_bound + pivot)//2
            print(f"pivot = {pivot}, lb = {lower_bound}, ub = {upper_bound}")
        if paired_pos is not None:
            break
        
    return paired_pos or (None, None)
    

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('search', metavar='search', type=int, help='The sum integer to find')
    args = parser.parse_args()

    input_lines = read_input(os.path.join(os.path.dirname(__file__),"../input.txt"))
    casted = [ int(x.strip()) for x in input_lines ]
    ordered = sorted(casted)

    num1, num2 = get_sum_pair(ordered, args.search)

    if num1 and num2:
        print("\n\n")
        print(f"Magic Numbers: {num1} + {num2} = {num1+num2}.")
        print(f"The solution is: {num1} x {num2} = {num1*num2}.")
    else:
        print("No valid pair found.")
