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

    def __repr__(self):
        sb = []
        ssb = []
        ssb.append("[")
        for light in self.lights:
            if light:
                ssb.append("#")
                continue
            ssb.append(".")
        ssb.append("]")
        sb.append("".join(ssb))
        ssb = []
        ssb.append("[")
        for target in self.targets:
            if target:
                ssb.append("#")
                continue
            ssb.append(".")
        ssb.append("]")
        sb.append("".join(ssb))
        return " ".join(sb)

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

class Buttons:
    def __init__(self, tokens):
        self.buttons = []
        for token in tokens:
            self.buttons.append(Button(token))

    def __repr__(self):
        sb = []
        for button in self.buttons:
            sb.append(str(button))
        return " ".join(sb)

class Machine:
    def __init__(self, s):
        tok = s.split(" ")
        self.panel = Panel(tok[0])
        self.buttons = Buttons(tok[1:len(tok)-1])

    def __repr__(self):
        sb = []
        sb.append(str(self.panel))
        sb.append(str(self.buttons))
        return " ".join(sb)

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
            

def main():
    print("Hello from part1!")

if __name__ == "__main__":
    main()
