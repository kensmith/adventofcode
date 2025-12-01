max_dial = 100

def main():
    password = 0
    pos = 50
    with open('input') as f:
        for line in f:
            d = line[0]
            n = int(line[1:])
            if d == 'R':
                pos += n
                pos %= max_dial
                if pos == 0:
                    password += 1
                continue
            if d != 'L':
                continue
            pos -= n
            pos %= max_dial
            if pos == 0:
                password += 1
    print(f'password = {password}')

if __name__ == "__main__":
    main()
