from itertools import product, combinations
from collections import defaultdict
import math

def parse_joltages(s):
    return list(map(int, s.strip().replace("{", "").replace("}", "").split(",")))

def parse_buttons(ss, n):
    button_values = []
    button_map = defaultdict(list)
    for s in ss:
        result = [0] * n
        keys = []
        for i in map(int, s.strip().replace(")", "").replace("(", "").split(",")):
            result[i] = 1
            keys.append(i)
        button_values.append(Joltages(result))
        for key in keys:
            button_map[key].append(Joltages(result))
    print(f"button_map = {button_map}")
    print(f"button_values = {button_values}")
    return button_values, button_map

class Joltages:
    def __init__(self, jj):
        self.jj = jj
    def __eq__(self, rhs):
        return self.jj == rhs.jj
    def __add__(self, rhs):
        self.jj = list(map(lambda x: x[0]+x[1], zip(self.jj, rhs.jj)))
        return self
    def __repr__(self):
        return "{" + ",".join(map(str, self.jj)) + "}"
    def __len__(self):
        return len(self.jj)
    def _inequality_helper(self, rhs):
        base = max(self.jj + rhs.jj)
        lhs_value = 0
        rhs_value = 0
        place = 0
        for p in zip(self.jj, rhs.jj):
            mul = math.pow(base, place)
            lhs_value += p[0]*mul
            rhs_value += p[1]*mul
            place += 1
        return lhs_value, rhs_value
    def __lt__(self, rhs):
        lhs_value, rhs_value = self._inequality_helper(rhs)
        return lhs_value < rhs_value
    def __gt__(self, rhs):
        lhs_value, rhs_value = self._inequality_helper(rhs)
        return lhs_value > rhs_value
    def __le__(self, rhs):
        lhs_value, rhs_value = self._inequality_helper(rhs)
        return int(lhs_value) <= int(rhs_value)
    def __ge__(self, rhs):
        lhs_value, rhs_value = self._inequality_helper(rhs)
        return int(lhs_value) > int(rhs_value)
    
class Machine:
    def __init__(self, s):
        tokens = s.split(" ")
        self.joltages = Joltages(parse_joltages(tokens[-1]))
        print(f"joltages = {self.joltages}")
        self.buttons, self.button_map = parse_buttons(tokens[1:len(tokens)-1], len(self.joltages))

    def adjust(self):
        # TODO use buttons to increment via list(map(lambda a:a[0]+a[1],zip(x,y)))
        # and use button_map to find candidate presses which affect a given button
        # use max(self.joltages) to limit iteration
        return 0

class Factory:
    def __init__(self, s):
        lines = s.strip().split("\n")
        self.machines = []
        for line in lines:
            self.machines.append(Machine(line))

    def adjust(self):
        result = 0
        for machine in self.machines:
            result += machine.adjust()
        return result

def main():
    with open("input") as f:
        f = Factory(f.read())

if __name__ == "__main__":
    main()
