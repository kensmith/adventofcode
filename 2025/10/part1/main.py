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
    return [] # part2

def parse_buttons(ss):
    results = []
    for s in ss:
        result = 0
        for i in map(int, s.strip().replace(")", "").replace("(", "").split(",")):
            result += math.pow(2, i)
        results.append(int(result))
    return results
    
class Machine:
    def __init__(self, s):
        tokens = s.split(" ")
        self.target = parse_target(tokens[0])
        self.joltages = parse_joltages(tokens[-1])
        self.buttons = parse_buttons(tokens[1:len(tokens)-1])

    def start(self):
        valid_seqs = []
        for i in range(1, len(self.buttons)):
            for seq in list(combinations(self.buttons, i)):
                result = 0
                for n in seq:
                    result ^= n
                if result == self.target:
                    valid_seqs.append(seq)
        seq_lengths = sorted(list(map(len, valid_seqs)))
        return seq_lengths[0]

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

def main():
    with open("input") as f:
        f = Factory(f.read())
        assert 461 == f.start()

if __name__ == "__main__":
    main()
