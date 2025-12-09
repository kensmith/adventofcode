from functools import cache
from itertools import pairwise, combinations
from collections import defaultdict

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
        print(self.width, self.height)
        self.colorize_border()
        self.interior = set()
        self.border_by_row = {}
        self.make_border_by_row()

    def make_border_by_row(self):
        self.border_by_row = defaultdict(list)
        for coord in self.red_set | self.border:
            y = coord[1]
            self.border_by_row[y].append(coord[0])
        for y in self.border_by_row:
            self.border_by_row[y].sort()
    
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
        y = coord[1]
        if y not in self.border_by_row:
            return False
        # Count runs of consecutive border points as single intersections
        border_xs = [x for x in self.border_by_row[y] if x < coord[0]]
        if not border_xs:
            return False
        intersections = 1  # First border point always starts a run
        for i in range(1, len(border_xs)):
            if border_xs[i] - border_xs[i-1] > 1:
                intersections += 1  # New run of border points
        return intersections % 2 == 1

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

    # DO NOT look in here. it's hideous
    def largest(self):
        areas = []
        for lhs, rhs in combinations(self.red, 2):
            areas.append((area(lhs,rhs), lhs, rhs))
        areas.sort()
        checked = 0
        for i in range(len(areas)-1, -1, -1):
            a, lhs, rhs = areas[i]
            ul, lr = idealized_corners(lhs, rhs)

            # center
            center = ((ul[0] + lr[0]) // 2, (ul[1] + lr[1]) // 2)
            if not self.is_interior(center):
                continue

            checked += 1
            if checked % 100 == 0:
                print(f"Checked {checked} candidates, current max area: {a}")

            # corners
            corners = [ul, lr, (ul[0], lr[1]), (lr[0], ul[1])]
            if not all(self.is_interior(c) for c in corners):
                continue

            all_interior = True
            width = lr[0] - ul[0] + 1
            height = lr[1] - ul[1] + 1

            # skip size
            y_step = max(1, height // 50)
            x_step = max(1, width // 50)

            # vertical edges
            for y in range(ul[1], lr[1]+1, y_step):
                if not self.is_interior((ul[0], y)) or not self.is_interior((lr[0], y)):
                    all_interior = False
                    break

            # belt and suspenders
            if all_interior and (lr[1] - ul[1]) % y_step != 0:
                if not self.is_interior((ul[0], lr[1])) or not self.is_interior((lr[0], lr[1])):
                    all_interior = False

            if not all_interior:
                continue

            # horizontal edges top and bottom edges (sampled)
            for x in range(ul[0], lr[0]+1, x_step):
                if not self.is_interior((x, ul[1])) or not self.is_interior((x, lr[1])):
                    all_interior = False
                    break

            # shoelaces
            if all_interior and (lr[0] - ul[0]) % x_step != 0:
                if not self.is_interior((lr[0], ul[1])) or not self.is_interior((lr[0], lr[1])):
                    all_interior = False

            if all_interior:
                return a
        print(f"Total candidates checked: {checked}")
        return 0

def main():
    with open('input') as f:
        f = Floor(f.read())
        result = f.largest()
        print(f"Largest rectangle area: {result}")


if __name__ == "__main__":
    main()
