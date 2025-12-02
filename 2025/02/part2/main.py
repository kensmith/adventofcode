import math

def is_odd(x):
    return x % 2 == 1

def to_int(candidate):
    return int(''.join([str(x) for x in candidate]))

def incr_fragment(fragment):
    n = to_int(fragment)
    n += 1
    result = []
    while n > 0:
        digit = n % 10
        result += [digit]
        n //= 10
    return result[::-1]

def invalid_ids(x, y):
    num_digits_x = math.ceil(math.log10(x))
    num_digits_y = math.ceil(math.log10(y))
    max_digits = max(num_digits_x, num_digits_y)
    ratio = 2
    result = set()
    while True:
        smallest_half_x = math.floor(max_digits / ratio)
        if smallest_half_x <= 0:
            break
        fragment = [1]
        smallest_half_x -= 1
        smallest_half_x = max(smallest_half_x, 0)
        fragment += [0] * smallest_half_x
        while True:
            candidate = fragment * ratio
            fragment = incr_fragment(fragment)
            n = to_int(candidate)
            if n < x:
                continue
            if x <= n and n <= y:
                result.add(n)
            if y < n:
                break
        ratio += 1
    return result

def main():
    with open("input") as f:
        content = f.read().strip()
        intervals = content.split(",")
        sum = 0
        for interval in intervals:
            pair = [int(x) for x in interval.split("-")]
            if len(pair) != 2:
                continue
            invalids = invalid_ids(pair[0], pair[1])
            for n in invalids:
                sum += n
        print(sum)


if __name__ == "__main__":
    main()
