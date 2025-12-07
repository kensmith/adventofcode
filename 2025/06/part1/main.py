functors = {"+": lambda x, y: x + y, "*": lambda x, y: x * y}

def get_tokens(s):
    tokens = []
    for token in s.strip().split(" "):
        token = token.strip()
        if "" == token:
            continue
        tokens.append(token)
    return tokens

def get_nums(s):
    tokens = get_tokens(s)
    nums = []
    for token in tokens:
        nums.append(int(token))
    return nums

def calculate(s):
    lines = s.strip().split("\n")
    lines.reverse()
    ops = get_tokens(lines[0])
    nums = get_nums(lines[1])
    for line in lines[2:]:
        n = get_nums(line)
        for i in range(len(n)):
            op = ops[i]
            nums[i] = functors[op](nums[i], n[i])
    return sum(nums)

def main():
    with open('input') as f:
        print(calculate(f.read()))

if __name__ == "__main__":
    main()
