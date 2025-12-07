from main import *

sample_input = """

3-5
10-14
16-20
12-18

1
5
8
11
17
32

"""

def test_sample():
    g = Ingredients(sample_input)
    assert 3 == g.are_fresh()


