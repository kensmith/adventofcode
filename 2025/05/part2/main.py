class Ingredients:
    def __init__(self, s):
        halves = s.strip().split("\n\n")
        assert 2 == len(halves)
        self.compute_intervals(halves[0])
        self.parse_ingredients(halves[1])
        for i in self.i:
            print(i)

    def compute_intervals(self, s):
        self.i = []
        for ss in s.split("\n"):
            lhs, rhs = ss.split("-")
            self.i.append((int(lhs), int(rhs)))
        self.collapse_intervals()

    def collapse_intervals(self):
        self.i.sort()
        new_i = [self.i[0]]
        for i in range(1, len(self.i)):
            p = len(new_i) - 1
            if self.i[i][0] <= new_i[p][1]:
                new_i[p] = (
                        new_i[p][0],
                        max(new_i[p][1], self.i[i][1]))
            else:
                new_i.append(self.i[i])
        self.i = new_i

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
                print(g)
                count += 1
        return count

    def fresh_ids(self):
        count = 0
        for i in self.i:
            count += i[1] - i[0] + 1
        return count


def main():
    with open("input") as f:
        g = Ingredients(f.read())
        print(f"fresh: {g.are_fresh()}") # 652
        # low  330426505855175
        # low  330426505855192
        # high 424424047587682
        print(f"fresh ids: {g.fresh_ids()}")


if __name__ == "__main__":
    main()
