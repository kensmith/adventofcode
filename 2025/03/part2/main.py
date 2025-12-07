"""
An escalator can never break: it can only become stairs. You should never see
an Escalator Temporarily Out Of Order sign, just Escalator Temporarily Stairs.
Sorry for the convenience.

Mitch Hedberg
"""

num_digits = 12

def to_int(arr):
    return int("".join(map(str, arr)))

def find_max(p, q, s):
    max_i = p
    max_n = int(s[max_i])
    for i in range(p+1, q+1):
        if int(s[i]) > max_n:
            max_i = i
            max_n = int(s[max_i])
    return max_i, max_n

def joltage(bank):
    bank_len = len(bank)
    left_i = 0
    right_i = bank_len - num_digits
    result = []
    for i in range(num_digits):
        max_i, max_n = find_max(left_i, right_i, bank)
        result += [max_n]
        left_i = max_i + 1
        right_i += 1
    return to_int(result)

def main():
    sum = 0
    with open("input") as f:
        for line in f:
            sum += joltage(line.strip())
    print(sum)

if __name__ == "__main__":
    main()
