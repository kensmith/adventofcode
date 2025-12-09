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

def test_sample():
    f = Floor(sample)
    assert 50 == f.largest()
