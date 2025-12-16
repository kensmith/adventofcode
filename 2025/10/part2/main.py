from itertools import product, combinations
from collections import defaultdict
import math
from copy import copy, deepcopy

def parse_joltages(s):
    return list(map(int, s.strip().replace("{", "").replace("}", "").split(",")))

def add(lhs, rhs):
    assert len(lhs) == len(rhs)
    return list(map(lambda x: x[0]+x[1], zip(lhs, rhs)))

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
    def __abs__(self):
        self.jj = list(map(abs, self.jj))
        return self
    def __eq__(self, rhs):
        return self.jj == rhs.jj
    def __add__(self, rhs):
        self.jj = list(map(lambda x: x[0]+x[1], zip(self.jj, rhs.jj)))
        return self
    def __sub__(self, rhs):
        self.jj = list(map(lambda x: x[0]-x[1], zip(self.jj, rhs.jj)))
        return self
    def __repr__(self):
        return "{" + ",".join(map(str, self.jj)) + "}"
    def __len__(self):
        return len(self.jj)
    def __int__(self):
        base = max(self.jj)
        place = 0
        result = 0
        for p in self.jj:
            mul = math.pow(base, place)
            result += p*mul
            place += 1
        return int(result)
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
    def solved_indices(self, rhs):
        result = []
        for i, x in enumerate(zip(self.jj, rhs.jj)):
            a = x[0]
            b = x[1]
            gap = abs(a - b)
            if gap == 0:
                result.append(i)
        return result
    def closest_index_with_gap(self, rhs):
        result = 0
        smallest = -1
        for i, x in enumerate(zip(self.jj, rhs.jj)):
            a = x[0]
            b = x[1]
            gap = abs(a - b)
            if gap > 0:
                if smallest < 0 or gap < smallest:
                    result = i
                    smallest = gap
                    continue
        return result
    def __getitem__(self, i):
        return self.jj[i]
    def __setitem__(self, i, n):
        assert(type(n) is int)
        self.jj[i] = n
    def __copy__(self):
        return Joltages(self.jj)
    def safest_button(self, buttons, i):
        # given the target index i, and the candidate buttons, find the button
        # which when pressed will have the least collateral effect
        sizes = []
        for button in buttons:
            b = copy(button)
            b[i] = 0
            sizes.append(int(self - b))
        print(f"sizes = {sizes}")
        return sizes.index(max(sizes))
    
class Machine:
    def __init__(self, s):
        tokens = s.split(" ")
        self.joltages = Joltages(parse_joltages(tokens[-1]))
        print(f"joltages = {self.joltages}")
        self.buttons, self.button_map = parse_buttons(tokens[1:len(tokens)-1], len(self.joltages))

    def adjust(self):
        while True:
            j = Joltages([0]*len(self.joltages))
            i = j.closest_index_with_gap(self.joltages)
            print(f"gap is at {i}")
            candidate_buttons = self.button_map[i]
            print(f"candidate buttons = {candidate_buttons}")
            distances_j = abs(self.joltages - j)
            print(f"distances_j = {distances_j}")
            safest = distances_j.safest_button(candidate_buttons, i)
            print(f"safest = {safest}")
            break

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
