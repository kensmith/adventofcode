sample = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""

def solve(s):
    pos = 50
    count = 0
    s = s.strip().split("\n")
    for r in s:
        v = int(r[1:])
        match r[0]:
            case 'R':
                pos += v
            case 'L':
                pos -= v
        pos %= 100
        if pos == 0:
            count += 1
    print(count)

def main():
    solve(sample)
    with open('input') as f:
        solve(f.read())


if __name__ == "__main__":
    main()
