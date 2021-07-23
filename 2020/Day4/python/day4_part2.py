import os
import re

class Passport:
    def __init__(self, fields) -> None:
        self.fields = {
            field.split(":")[0] : field.split(":")[1].rstrip("\n")
            for field in fields
        }
    
    def validate(self):
        if not self.validate_fields():
            return False
        return all([
            self.validate_byr(),
            self.validate_iyr(),
            self.validate_eyr(),
            self.validate_hgt(),
            self.validate_hcl(),
            self.validate_ecl(),
            self.validate_pid(),
        ])

    def validate_fields(self):
        if len(self.fields.keys()) < 7:
            return False
        else:
            expected = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
            keys = set(self.fields.keys())
            diff = expected.difference(keys)

            return (diff == set())
    
    def validate_byr(self):
        byr = self.fields.get("byr")
        if byr:
            return 1920 <= int(byr) <= 2002
        return False
    
    def validate_iyr(self):
        iyr = self.fields.get("iyr")
        if iyr:
            return 2010 <= int(iyr) <= 2020
        return False

    
    def validate_eyr(self):
        eyr = self.fields.get("eyr")
        if eyr:
            return 2020 <= int(eyr) <= 2030
        return False
    
    def validate_hgt(self):
        hgt = self.fields.get("hgt")
        rgx = re.compile(r"([0-9]{2,3})(cm|in)")
        if hgt:
            m = rgx.match(hgt)
            if m:
                if m[2] == "cm":
                    return 150 <= int(m[1]) <= 193
                else:
                    return 59 <= int(m[1]) <= 76
        return False
    
    def validate_hcl(self):
        hcl = self.fields.get("hcl")
        rgx = re.compile(r"#[0-9a-f]{6}")
        if hcl:
            return bool(rgx.match(hcl))
        return False
    
    def validate_ecl(self):
        ecl = self.fields.get("ecl")
        return ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        
    def validate_pid(self):
        pid = self.fields.get("pid")
        if pid:
            return (pid.isdigit() and len(pid) == 9)
        return False


if __name__ == "__main__":
    filepath = os.path.join(os.path.dirname(__file__), "../input.txt")

    valid = 0
    fields = []
    with open(filepath) as f:
        for line in f.readlines():
            if line == "\n" and fields != []:
                p = Passport(fields)
                valid += int(p.validate())
                fields = []
            else:
                fields.extend(line.split(" "))
    p = Passport(fields)
    valid += int(p.validate())
    print(valid)