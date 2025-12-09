from itertools import pairwise

def incr(x, rhs):
    if x[0] < rhs[0]:
        return (x[0]+1, x[1])
    if x[0] > rhs[0]:
        return (x[0]-1, x[1])
    if x[1] < rhs[1]:
        return (x[0], x[1]+1)
    if x[1] > rhs[1]:
        return (x[0], x[1]-1)

class Floor:
    def __init__(self, s):
        lines = s.strip().split("\n")
        self.width = 0
        self.height = 0
        self.red = []
        self.red_set = set()
        for line in lines:
            lhs, rhs = line.split(",")
            coord = (int(lhs), int(rhs))
            self.red.append(coord)
            self.red_set.add(coord)
            self.width = max(self.width, coord[0])
            self.height = max(self.height, coord[1])
        self.width += 1
        self.height += 1
        self.colorize_border()
        self.flood_exterior()
    
    def __repr__(self):
        lines = []
        for y in range(self.height):
            line = []
            for x in range(self.width):
                coord = (x, y)
                if coord not in self.exterior:
                    line.append('X')
                    continue
                line.append('.')
            lines.append(''.join(line))
        return '\n'.join(lines)


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

    def is_interior(self, coord):
        return coord not in self.exterior

    def is_border(self, coord):
        if coord in self.red_set:
            return True
        if coord in self.border:
            return True
        return False

    def flood_exterior(self):
        stack = []
        for y in range(self.height):
            print('computing vertical borders')
            for x in (0, self.width - 1):
                coord = (x, y)
                if not self.is_border(coord):
                    stack.append(coord)
        for x in range(self.width):
            print('computing horizontal borders')
            for y in (0, self.height - 1):
                coord = (x, y)
                if not self.is_border(coord):
                    stack.append(coord)

        print("starting flood")
        self.exterior = set()
        while stack:
            print(len(stack))
            coord = stack.pop()
            if coord in self.exterior or self.is_border(coord):
                continue

            x,y = coord
            if x < 0 or x >= self.width:
                continue
            if y < 0 or y >= self.height:
                continue

            self.exterior.add(coord)

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                stack.append((x+dx, y+dy))

    def largest(self):
        return 0

    def area(self, lhs, rhs):
        width = abs(rhs[0] - lhs[0]) + 1
        height = abs(rhs[1] - lhs[1]) + 1
        area = width * height
        return area

def main():
    with open('input') as f:
        f = Floor(f.read())
        print(f)
        print(f.largest())


if __name__ == "__main__":
    main()
