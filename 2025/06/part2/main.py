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

def transform(lines):
    max_line = max(map(len, lines))
    nums = [""] * int(max_line)
    for line in lines:
        for i, c in enumerate(line):
            nums[i] += c
    return nums

def calculate(s):
    lines = list(filter(lambda x: len(x) > 0, s.split("\n")))
    num_lines = len(lines)
    ops = get_tokens(lines[num_lines-1])
    tlines = transform(lines[:-1])
    i = 0
    j = 0
    results = []
    while i < len(ops):
        nums = []
        while j < len(tlines) and tlines[j].strip() != "":
            nums.append(int(tlines[j]))
            j += 1
        if len(nums) == 0:
            j += 1
            continue
        result = nums[0]
        for num in nums[1:]:
            result = functors[ops[i]](result, num)
        results.append(result)
        i += 1
    return sum(results)

def main():
    with open("input") as f:
        print(calculate(f.read()))

if __name__ == "__main__":
    main()
