import os

def go_down_the_slope(input_path, rows, input_columns, right, down):
    x,y = 0,0
    pos = y*input_columns + x%input_columns
    trees = 0
    while True:
        trees += input_path[pos]
        y += down
        x += right
        pos = y*input_columns + x%input_columns
        if y >= rows:
            break

    return trees

def test_slopes(input_path, rows, input_columns, slopes):
    mul = 1
    for right, down in slopes:
        trees = go_down_the_slope(input_path, rows, input_columns, right, down)
        print("SLOPE [R:{}, D:{}] - I have encountered {} trees".format(
            right, down, trees
        ))
        mul = mul * trees
    print("All trees multiplied together give: {}".format(mul))


if __name__ == "__main__":
    file = open(os.path.join(os.path.dirname(__file__), "../input.txt"), 'r')

    rows = 0
    input_columns = -1
    input_path = []
    while True:
        char = file.read(1)
        if char == '#':
            input_path.append(1)
        elif char == '.':
            input_path.append(0)
        elif char == '\n':
            if input_columns == -1:
                input_columns = len(input_path)
            rows += 1
        if not char:
            break
    
    file.close()

    print("Input Size: ")
    print("input_columns = {}".format(input_columns))
    print("input_rows = {}".format(rows))

    test_slopes(
        input_path,
        rows, 
        input_columns,
        [   (1,1),
            (3,1),
            (5,1),
            (7,1),
            (1,2),
        ]
    )


    
    
    






