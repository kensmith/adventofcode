class Grid:
    max_bales = 4
    def __init__(self, s):
        lines = s.strip().split("\n")
        self.height =  len(lines)
        self.width = len(lines[0])
        assert self.height > 0
        assert self.width > 0
        self.grid = "".join(lines)
        self.grid_len = len(self.grid)

    def __repr__(self):
        sb = []
        for i in range(0, self.grid_len, self.width):
            sb += [self.grid[i:i+self.width]]
        return "\n".join(sb)

    def L(self, x, y):
        return x == 0

    def R(self, x, y):
        return x == self.width - 1

    def T(self, x, y):
        return y == 0

    def B(self, x, y):
        return y == self.height - 1

    def _clip(self, x, y, indices):
        # 0  1  2
        # 3     4
        # 5  6  7
        assert(len(indices) == 8)
        if self.L(x, y) and self.T(x, y):
            indices = [indices[4]] + indices[6:8]
        elif self.L(x, y) and not self.T(x, y) and not self.B(x, y):
            indices = indices[1:3] + [indices[4]] + indices[6:8]
        elif self.L(x, y) and self.B(x, y):
            indices = indices[1:3] + [indices[4]]
        elif self.R(x, y) and self.T(x, y):
            indices = [indices[3]] + indices[5:7]
        elif self.R(x, y) and not self.T(x, y) and not self.B(x, y):
            indices = indices[0:2] + [indices[3]] + indices[5:7]
        elif self.R(x, y) and self.B(x, y):
            indices = indices[0:2] + [indices[3]]
        elif self.T(x, y) and not self.L(x, y) and not self.R(x, y):
            indices = indices[3:8]
        elif self.B(x, y) and not self.L(x, y) and not self.B(x, y):
            indices = indices[:5]

        indices = list(filter(lambda x: x >= 0 and x < self.grid_len, indices))
        return indices

    def coord_to_i(self, x, y):
        return y * self.width + x

    def neighbors(self, x, y):
        i = self.coord_to_i(x, y)
        indices = list(range(i - self.width - 1, i - self.width + 2))
        indices += [i - 1, i + 1]
        indices += list(range(i + self.width - 1, i + self.width + 2))
        indices = self._clip(x, y, indices)
        n = list(map(lambda x: self.grid[x], indices))
        return n

    def can_access(self, x, y):
        if self.element(x, y) != "@":
            return False
        n = self.neighbors(x, y)
        p = list(filter(lambda x: x == "@", n))
        return len(p) < self.max_bales

    def element(self, x, y):
        i = self.coord_to_i(x, y)
        assert i >= 0
        assert i < self.grid_len
        return self.grid[i]

    def paper_positions(self):
        result = []
        for x in range(self.width):
            for y in range(self.height):
                if self.element(x, y) == "@":
                    result += [(x, y)]
        return result

    def accessible_paper(self):
        o = self.paper_positions()
        acc = list(filter(lambda x: self.can_access(*x), o))
        return acc

    def remove_paper(self, x, y):
        assert self.element(x, y) == '@'
        i = self.coord_to_i(x, y)

        # gc stress test, lol
        self.grid = self.grid[:i] + '.' + self.grid[i+1:]

    def remove_accessible_paper(self):
        accessible = self.accessible_paper()
        num_removed = len(accessible)
        for pair in accessible:
            self.remove_paper(*pair)
        return num_removed

    def remove_all_paper(self):
        orig_num_accessible = len(self.accessible_paper())
        total = 0
        removed = 1
        while removed > 0:
            removed = self.remove_accessible_paper()
            total += removed
            print(f"removed = {removed}, total = {total}")
        return total

def main():
    with open('input') as f:
        grid = Grid(f.read())
        total = grid.remove_all_paper()
        print(f"removed {total} papers")

if __name__ == "__main__":
    main()
