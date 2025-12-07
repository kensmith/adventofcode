class Ingredients:
    def __init__(self, s):
        halves = s.strip().split("\n\n")
        assert 2 == len(halves)
        self.compute_intervals(halves[0])
        self.parse_ingredients(halves[1])

    def compute_intervals(self, s):
        self.i = []
        for ss in s.split("\n"):
            lhs, rhs = ss.split("-")
            self.i.append((int(lhs), int(rhs)))
        self.collapse_intervals()

    def collapse_intervals(self):
        ...

    def parse_ingredients(self, s):
        self.g = []
        for ss in s.split("\n"):
            self.g.append(int(ss))

    def is_fresh(self, g):
        for i in self.i:
            if i[0] <= g and g <= i[1]:
                return True
        return False

    def are_fresh(self):
        count = 0
        for g in self.g:
            if self.is_fresh(g):
                count += 1
        return count

def main():
    with open("input") as f:
        g = Ingredients(f.read())
        print(g.are_fresh())


if __name__ == "__main__":
    main()
