from itertools import combinations

class Floor:
    def __init__(self, s):
        lines = s.strip().split("\n")
        self.red = []
        for line in lines:
            lhs, rhs = line.split(",")
            self.red.append((int(lhs), int(rhs)))
        self.areas = sorted([self.area(a, b) for a, b in combinations(self.red, 2)])

    def largest(self):
        return self.areas[-1]

    def area(self, lhs, rhs):
        width = abs(rhs[0] - lhs[0]) + 1
        height = abs(rhs[1] - lhs[1]) + 1
        area = width * height
        return area

def main():
    with open('input') as f:
        f = Floor(f.read())
        print(f.largest())


if __name__ == "__main__":
    main()
