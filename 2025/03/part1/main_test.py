import pytest
from main import *

def test_joltage():
    print("")
    assert 98 == joltage("987654321111111")
    assert 89 == joltage("811111111111119")
    assert 78 == joltage("234234234234278")
    assert 92 == joltage("818181911112111")
