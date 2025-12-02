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
    if num_digits_x == num_digits_y:
        if is_odd(num_digits_x):
            return []
    smallest_half_x = math.ceil(num_digits_x / 2.0)
    smallest_half_y = math.ceil(num_digits_y / 2.0)
    fragment = [1]
    smallest_half_x -= 1
    smallest_half_x = max(smallest_half_x, 0)
    fragment += [0] * smallest_half_x
    result = []
    while True:
        candidate = fragment * 2
        fragment = incr_fragment(fragment)
        n = to_int(candidate)
        if n < x:
            continue
        if x <= n and n <= y:
            result += [n]
        if y < n:
            break
    return result

def main():
    print("main")

if __name__ == "__main__":
    main()
