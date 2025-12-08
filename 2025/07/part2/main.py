from functools import cache

class Manifold:
    def __init__(self, s):
        self.s = list(map(list, s.strip().split("\n")))
        self.find_emitter()

    @cache
    def rows(self):
        return len(self.s)

    def __repr__(self):
        r = []
        for s in self.s:
            r.append("".join(s))
        return "\n".join(r)

    def find_emitter(self):
        for i, c in enumerate(self.s[0]):
            if c == "S":
                self.emitter = i

    def fire(self):
        return self.fire_helper(self.emitter, 0)

    @cache
    def fire_helper(self, x, y):
        if y >= self.rows() - 1:
            return 1

        ny = y + 1
        if self.s[ny][x] == "^":
            return self.fire_helper(x-1, ny) + self.fire_helper(x+1, ny)

        return self.fire_helper(x, ny)

def main():
    with open("input") as f:
        m = Manifold(f.read())
        print(m.fire())

if __name__ == "__main__":
    main()
