import math

def distance(lhs, rhs):
    terms = []
    for a, b in zip(lhs, rhs):
        a -= b
        terms.append(a*a)

    return math.sqrt(sum(terms))

class Junctions:
    def __init__(self, s):
        coords = []
        coordStrs = s.strip().split("\n")
        for coordStr in coordStrs:
            x, y, z = map(int, coordStr.split(","))
            coords.append((x,y,z))

        self.dists = []
        for i in range(len(coords)):
            for j in range(i+1, len(coords)):
                dist = distance(coords[i], coords[j])
                self.dists.append((dist, coords[i], coords[j]))
        self.dists.sort()

    def connect(self, n):
        ss = []
        for i in range(n):
            dist, lhs, rhs = self.dists[i]
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
        ls = list(map(len, ss))
        ls.sort()
        result = 1
        for i in range(-1, -4, -1):
            result *= ls[i]
        return result

def main():
    with open("input") as f:
        j = Junctions(f.read())
        print(j.connect(1000))


if __name__ == "__main__":
    main()
