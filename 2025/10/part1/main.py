from itertools import product

class Panel:
    def __init__(self, s):
        s = s.strip().replace("]","")
        s = s.strip().replace("[","")
        self.lights = []
        self.targets = []
        for c in s:
            assert c in ".#"
            self.lights.append(0)
            if c == ".":
                self.targets.append(0)
                continue
            self.targets.append(1)

    def repr_helper(self, things):
        sb = []
        sb.append("[")
        for thing in things:
            if thing:
                sb.append("#")
                continue
            sb.append(".")
        sb.append("]")
        return "".join(sb)

    def __repr__(self):
        sb = []
        sb.append(self.repr_helper(self.lights))
        sb.append(self.repr_helper(self.targets))
        return " ".join(sb)

    def solved(self):
        for light, target in zip(self.lights, self.targets):
            if light != target:
                return False
        return True

class Button:
    def __init__(self, s):
        s = s.strip().replace(")", "")
        s = s.strip().replace("(", "")
        self.toggles = list(map(int, s.split(",")))

    def __repr__(self):
        sb = []
        for toggle in self.toggles:
            sb.append(str(toggle))
        return "(" + ",".join(sb) + ")"

class Machine:
    def __init__(self, s):
        tokens = s.split(" ")
        self.panel = Panel(tokens[0])
        self.buttons = []
        for token in tokens[1:len(tokens)-1]:
            self.buttons.append(Button(token))

    def __repr__(self):
        sb = []
        sb.append(str(self.panel))
        sb.append(str(self.buttons))
        return " ".join(sb)

    def mash_buttons(self):
        print(self.buttons)
        return 0

class Factory:
    def __init__(self, s):
        self.machines = []
        lines = s.strip().split("\n")
        for line in lines:
            self.machines.append(Machine(line))

    def __repr__(self):
        sb = []
        for m in self.machines:
            sb.append(str(m))
        return "\n".join(sb)

    def mash_buttons(self):
        total = 0
        for machine in self.machines:
            total += machine.mash_buttons()
        return total

def main():
    print("Hello from part1!")

if __name__ == "__main__":
    main()
