import os

def validate(fields):
    if len(fields) < 7:
        return False
    else:
        expected = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
        keys = set([pair.split(":")[0] for pair in fields])

        diff = expected.difference(keys)

        return (diff == set())


if __name__ == "__main__":
    filepath = os.path.join(os.path.dirname(__file__), "../input.txt")

    valid = 0
    fields = []
    with open(filepath) as f:
        for line in f.readlines():
            if line == "\n" and fields != []:
                valid += int(validate(fields))
                fields = []
            else:
                fields.extend(line.split(" "))
    valid += int(validate(fields))
    print(valid)