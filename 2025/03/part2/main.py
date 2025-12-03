"""
An escalator can never break: it can only become stairs. You should never see
an Escalator Temporarily Out Of Order sign, just Escalator Temporarily Stairs.
Sorry for the convenience.

Mitch Hedberg
"""

import heapq

num_digits = 12

def to_int(arr):
    mult = 1
    result = 0
    for i in range(len(arr) - 1, -1, -1):
        result += int(arr[i]) * mult
        mult *= 10
    return result

def joltage(bank):
    bank_len = len(bank)
    assert bank_len > num_digits
    heap = []
    for i in range(bank_len):
        heapq.heappush_max(heap, (bank[i], i))
    result_digits = [0] * bank_len
    for i in range(num_digits):
        digit = heapq.heappop_max(heap)
        if len(digit) < 2:
            break
        result_digits[digit[1]] = digit[0]
    result = [x for x in result_digits if x != 0]
    return to_int(result)
        


def main():
    sum = 0
    #with open("input") as f:
    #    for line in f:
    #        sum += joltage(line.strip())
    print(sum)

if __name__ == "__main__":
    main()
