import os

if __name__ == "__main__":
    filepath = os.path.join(os.path.dirname(__file__), "../input.txt")

    increased_times = 0
    prev = None
    with open(filepath) as f:
        for line in f.readlines():
            current = int(line.strip("\n"))
            if prev is not None:
                increased_times = increased_times + int((current-prev) > 0)
            prev = current
    
    print(f"It has increased {increased_times} times")