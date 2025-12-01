import pytest
from main import Dial

def test_r_basic():
    d = Dial()
    d.add("R50")
    assert d.pos == 0
    assert d.password == 1

    d.add("R1000")
    assert d.pos == 0
    assert d.password == 11

def test_sample():
    d = Dial()
    d.add("L68")
    assert d.pos == 82
    assert d.password == 1

    d.add("L30")
    assert d.pos == 52
    assert d.password == 1

    d.add("R48")
    assert d.pos == 0
    assert d.password == 2

    d.add("L5")
    assert d.pos == 95
    assert d.password == 2

    d.add("R60")
    assert d.pos == 55
    assert d.password == 3

    d.add("L55")
    assert d.pos == 0
    assert d.password == 4

    d.add("L1")
    assert d.pos == 99
    assert d.password == 4

    d.add("L99")
    assert d.pos == 0
    assert d.password == 5

    d.add("R14")
    assert d.pos == 14
    assert d.password == 5

    d.add("L82")
    assert d.pos == 32
    assert d.password == 6

