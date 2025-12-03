"""
An escalator can never break: it can only become stairs. You should never see
an Escalator Temporarily Out Of Order sign, just Escalator Temporarily Stairs.
Sorry for the convenience.

Mitch Hedberg
"""

num_digits = 2

def to_int(arr):
    return int(arr[0]) * 10 + int(arr[1])

def joltage(bank):
    max_left_pos = 0
    max_left = bank[max_left_pos]
    for i in range(max_left_pos + 1, len(bank) - 1):
        if bank[i] > max_left:
            max_left_pos = i
            max_left = bank[i]
    max_right_pos = len(bank) - 1
    max_right = bank[max_right_pos]
    for i in range(max_right_pos - 1, max_left_pos, -1):
        if bank[i] > max_right:
            max_right_pos = i
            max_right = bank[i]

    return to_int([max_left, max_right])


def main():
    sum = 0
    with open("input") as f:
        for line in f:
            sum += joltage(line.strip())
    print(sum)

if __name__ == "__main__":
    main()
