import pytest
from main import *

def test_to_int():
    assert 1 == to_int([1])
    assert 12 == to_int([1, 2])
    assert 123 == to_int([1, 2, 3])


def test_joltage():
    print("")
    #joltage("987654321111111")
    assert 987654321111 == joltage("987654321111111")
    assert 811111111119 == joltage("811111111111119")
    assert 434234234278 == joltage("234234234234278")
    assert 888911112111 == joltage("818181911112111")
