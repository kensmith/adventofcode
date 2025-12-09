from functools import cache
from itertools import pairwise, combinations

def incr(x, rhs):
    if x[0] < rhs[0]:
        return (x[0]+1, x[1])
    if x[0] > rhs[0]:
        return (x[0]-1, x[1])
    if x[1] < rhs[1]:
        return (x[0], x[1]+1)
    if x[1] > rhs[1]:
        return (x[0], x[1]-1)

def area(lhs, rhs):
    width = abs(rhs[0] - lhs[0]) + 1
    height = abs(rhs[1] - lhs[1]) + 1
    area = width * height
    return area

@cache
def idealized_corners(lhs, rhs):
    return (
            (min(lhs[0], rhs[0]), min(lhs[1], rhs[1])),
            (max(lhs[0], rhs[0]), max(lhs[1], rhs[1]))
            )

class Floor:
    def __init__(self, s):
        lines = s.strip().split("\n")
        self.width = 0
        self.height = 0
        self.red = []
        self.red_set = set()
        for line in lines:
            lhs, rhs = map(int, line.split(","))
            coord = (lhs, rhs)
            self.red.append(coord)
            self.red_set.add(coord)
            self.width = max(self.width, coord[0])
            self.height = max(self.height, coord[1])
        self.width += 1
        self.height += 1
        self.colorize_border()
        self.interior = set()
    
    def __repr__(self):
        lines = []
        for y in range(self.height):
            line = []
            for x in range(self.width):
                coord = (x, y)
                if self.is_interior(coord):
                    line.append('I')
                    continue
                line.append('.')
            lines.append(''.join(line))
        return '\n'.join(lines)

    @cache
    def is_interior(self, coord):
        if self.is_border(coord):
            return True
        on_border = False
        intersections = 0
        for x in range(coord[0], -1, -1):
            c = (x, coord[1])
            if self.is_border(c):
                if not on_border:
                    on_border = True
                    intersections += 1
            else:
                on_boarder = False
        internal = intersections % 2 == 1
        return internal

    def colorize_border(self):
        self.border = set()
        start = self.red[0]
        for lhs, rhs in pairwise(self.red):
            self.colorize_between(lhs, rhs)
        self.colorize_between(rhs, start)

    def colorize_between(self, lhs, rhs):
        while lhs != rhs:
            lhs = incr(lhs, rhs)
            if lhs not in self.red_set:
                self.border.add(lhs)

    @cache
    def is_border(self, coord):
        if coord in self.red_set:
            return True
        if coord in self.border:
            return True
        return False

    def largest(self):
        areas = []
        for lhs, rhs in combinations(self.red, 2):
            areas.append((area(lhs,rhs), lhs, rhs))
        areas.sort()
        result = -1
        for i in range(len(areas)-1, -1, -1):
            a, lhs, rhs = areas[i]
            print(f"hi = {a}, {lhs}, {rhs}")
            ul, lr = idealized_corners(lhs, rhs)
            all_interior = True
            print("vertical borders")
            for y in range(ul[1], lr[1]+1):
                left_x = ul[0]
                right_x = lr[0]
                if not self.is_interior((left_x, y)):
                    all_interior = False
                    break
                if not self.is_interior((right_x, y)):
                    all_interior = False
                    break
            print("horizontal borders")
            for x in range(ul[0], lr[0]+1):
                top_y = ul[1]
                bottom_y = lr[1]
                if not self.is_interior((x, top_y)):
                    all_interior = False
                    break
                if not self.is_interior((x, bottom_y)):
                    all_interior = False
                    break

            if all_interior:
                result = a
        return result

def main():
    with open('input') as f:
        f = Floor(f.read())
        #print(f)
        print(f.largest())


if __name__ == "__main__":
    main()
