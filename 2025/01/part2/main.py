class Dial:
    pos = 50
    password = 0
    max_dial = 100

    def __init__(self):
        ...

    def right(self, n):
        new_pos = self.pos + n
        if new_pos >= self.max_dial:
            self.password += new_pos // self.max_dial
        if new_pos == 0:
            self.password += 1
            if self.pos == 0:
                self.password -= 1
        self.pos = new_pos % self.max_dial

    def add(self, line):
        line = line.strip()
        d = line[0]
        n = int(line[1:])
        match d:
            case "R":
                self.right(n)
            case "L":
                self.pos = (self.max_dial - self.pos) % self.max_dial
                self.right(n)
                self.pos = (self.max_dial - self.pos) % self.max_dial
            case _:
                raise Exception()

def main():
    d = Dial()
    with open("input") as f:
        for line in f:
            d.add(line)

    print(f"password = {d.password}")

if __name__ == "__main__":
    main()
