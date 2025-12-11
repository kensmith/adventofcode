from itertools import product, combinations
from collections import defaultdict
import math

def parse_target(s):
    s = s.strip().replace("[","").replace("]", "")
    result = 0
    for i, c in enumerate(s):
        if c == "#":
            result += math.pow(2, i)
    return int(result)

def parse_joltages(s):
    return list(map(int, s.strip().replace("{", "").replace("}", "").split(",")))

def parse_buttons_as_ints(ss):
    results = []
    for button in parse_buttons_as_lists(ss):
        result = 0
        for i in button:
            result += math.pow(2, i)
        results.append(int(result))
    return results

def parse_buttons_as_lists(ss):
    result = []
    for s in ss:
        result.append(list(map(int, s.strip().replace(")", "").replace("(", "").split(","))))
    return result
    
class Machine:
    def __init__(self, s):
        tokens = s.split(" ")
        self.target = parse_target(tokens[0])
        self.joltages = parse_joltages(tokens[-1])
        self.button_ints = parse_buttons_as_ints(tokens[1:len(tokens)-1])
        self.button_lists = parse_buttons_as_lists(tokens[1:len(tokens)-1])
        print(self.button_lists)

    def start(self):
        valid_seqs = []
        for i in range(1, len(self.button_ints)):
            for seq in list(combinations(self.button_ints, i)):
                result = 0
                for n in seq:
                    result ^= n
                if result == self.target:
                    valid_seqs.append(seq)
        seq_lengths = sorted(list(map(len, valid_seqs)))
        return seq_lengths[0]

    def adjust(self):
        ...

class Factory:
    def __init__(self, s):
        lines = s.strip().split("\n")
        self.machines = []
        for line in lines:
            self.machines.append(Machine(line))

    def start(self):
        result = 0
        for machine in self.machines:
            result += machine.start()
        return result

    def adjust(self):
        result = 0
        for machine in self.machines:
            result += machine.adjust()
        return result

def main():
    with open("input") as f:
        f = Factory(f.read())
        assert 461 == f.start()

if __name__ == "__main__":
    main()
