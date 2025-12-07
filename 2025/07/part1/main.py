class Manifold:
    def __init__(self, s):
        self.s = list(map(list, s.strip().split("\n")))
        self.find_emitter()

    def find_emitter(self):
        for i, c in enumerate(self.s[0]):
            if c == "S":
                self.emitter = i
                print(f"emitter = {i}")

    def fire(self):
        beams = {self.emitter}
        splits = 0
        for i in range(1,len(self.s)):
            print(i, beams)
            new_beams = set()
            for beam in beams:
                if self.s[i][beam] == "^":
                    splits += 1
                    new_beams.add(beam-1)
                    new_beams.add(beam+1)
                else:
                    new_beams.add(beam)
            beams = new_beams
        return splits


def main():
    with open("input") as f:
        m = Manifold(f.read())
        print(m.fire())

if __name__ == "__main__":
    main()
