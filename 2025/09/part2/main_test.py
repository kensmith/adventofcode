from main import *

sample = """
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
"""

"""
............
.......IIIII
.......IIIII
..IIIIIIIIII
..IIIIIIIIII
..IIIIIIIIII
.........III
.........III
"""

def test_sample():
    print("")
    f = Floor(sample)
    print(f)
    assert 24 == f.largest()
