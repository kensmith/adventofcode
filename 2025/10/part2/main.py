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
        button_values.append(result)
        for key in keys:
            button_map[key].append(result)
    print(button_map)
    return button_values, button_map
    
class Machine:
    def __init__(self, s):
        tokens = s.split(" ")
        self.joltages = parse_joltages(tokens[-1])
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
