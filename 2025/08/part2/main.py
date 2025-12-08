import math

def distance(lhs, rhs):
    terms = []
    for a, b in zip(lhs, rhs):
        a -= b
        terms.append(a*a)

    return math.sqrt(sum(terms))

class Junctions:
    def __init__(self, s):
        self.coords = []
        coordStrs = s.strip().split("\n")
        for coordStr in coordStrs:
            x, y, z = map(int, coordStr.split(","))
            self.coords.append((x,y,z))

        self.dists = []
        for i in range(len(self.coords)):
            for j in range(i+1, len(self.coords)):
                dist = distance(self.coords[i], self.coords[j])
                self.dists.append((dist, self.coords[i], self.coords[j]))
        self.dists.sort()

    def connect(self):
        ss = []
        i = 0
        while len(ss) == 0 or len(ss[0]) < len(self.coords):
            dist, lhs, rhs = self.dists[i]
            i += 1
            foundLhs = -1
            foundRhs = -1
            for j in range(len(ss)):
                if lhs in ss[j]:
                    foundLhs = j
                if rhs in ss[j]:
                    foundRhs = j
            if foundLhs < 0 and foundRhs < 0:
                ss.append({lhs, rhs})
                continue
            if foundLhs < 0 and foundRhs >=0:
                ss[foundRhs].add(lhs)
                continue
            if foundLhs >= 0 and foundRhs < 0:
                ss[foundLhs].add(rhs)
                continue
            if foundLhs == foundRhs:
                continue
            ss[foundLhs] |= ss[foundRhs]
            del ss[foundRhs]
        return lhs[0] * rhs[0]

def main():
    with open("input") as f:
        j = Junctions(f.read())
        print(j.connect())


if __name__ == "__main__":
    main()
