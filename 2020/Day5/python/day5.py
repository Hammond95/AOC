import os

def seat_conv(seat):
    row = seat[:7]
    col = seat[7:]
    rowbin = row.replace("F","0").replace("B","1")
    colbin = col.replace("L","0").replace("R","1")

    return int(rowbin, 2), int(colbin, 2)


if __name__ == "__main__":
    filepath = os.path.join(os.path.dirname(__file__), "../input.txt")

    seat_map = {}
    seat_ids = []
    with open(filepath) as f:
        for line in f.readlines():
            row, col = seat_conv(line.rstrip("\n"))
            seat_id = (row*8)+col
            seat_map[seat_id] = (row, col)
            seat_ids.append(seat_id)
    
    if seat_ids:
        print("Max Seat Id:", max(seat_ids))

    print("Missing id in seats:")
    seat_ids = sorted(seat_ids)
    for i in range(1, len(seat_ids)-1):
        if (seat_ids[i-1]+1 != seat_ids[i]) or (seat_ids[i+1]-1 != seat_ids[i]):
            print(
                seat_ids[i-1], seat_ids[i], seat_ids[i+1]
            )

