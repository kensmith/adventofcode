from itertools import product
from collections import defaultdict

class Panel:
    def __init__(self, s):
        s = s.strip().replace("]","")
        s = s.strip().replace("[","")
        self._lights = []
        self._targets = []
        for c in s:
            assert c in ".#"
            self._lights.append(0)
            if c == ".":
                self._targets.append(0)
                continue
            self._targets.append(1)

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
        sb.append(self.repr_helper(self._lights))
        sb.append(self.repr_helper(self._targets))
        return " ".join(sb)

    def lights(self):
        return list(map(lambda x: x[0], filter(lambda x: x[1], enumerate(self._lights))))

    def targets(self):
        return list(map(lambda x: x[0], filter(lambda x: x[1], enumerate(self._targets))))

    def solved(self):
        return self.lights() == self.targets()

class Button:
    def __init__(self, s):
        s = s.strip().replace(")", "")
        s = s.strip().replace("(", "")
        self._toggles = list(map(int, s.split(",")))

    def __repr__(self):
        sb = []
        for toggle in self._toggles:
            sb.append(str(toggle))
        return "(" + ",".join(sb) + ")"

    def toggles(self):
        return self._toggles

class Machine:
    def __init__(self, s):
        tokens = s.split(" ")
        self.panel = Panel(tokens[0])
        self.buttons = []
        self.button_map = defaultdict(list)
        for token in tokens[1:len(tokens)-1]:
            button = Button(token)
            self.buttons.append(button)
            for toggle in button.toggles():
                self.button_map[toggle].append(button)

    def __repr__(self):
        sb = []
        sb.append(str(self.panel))
        sb.append(str(self.buttons))
        return " ".join(sb)

    def mash_buttons(self):
        print(self.panel.targets())
        print(self.panel.lights())
        print(self.panel.solved())
        print(self.button_map)
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
