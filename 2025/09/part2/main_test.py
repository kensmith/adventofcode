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
.......XXXXX
.......XIIIX
..XXXXXX...X
..XIIIIIIIIX
..XXXXXXXX.X
.........XIX
.........XXX
"""

def test_sample():
    print("")
    f = Floor(sample)
    print(f)
    print(f.largest())
