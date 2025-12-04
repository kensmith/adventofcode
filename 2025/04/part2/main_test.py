from main import *

# ..xx.xx@x.
# x@@.@.@.@@
# @@@@@.x.@@
# @.@@@@..@.
# x@.@@@@.@x
# .@@@@@@@.@
# .@.@.@.@@@
# x.@@@.@@@@
# .@@@@@@@@.
# x.x.@@@.x.

# ..AA.AA@A.
# x@@.@.@.@@
# @@@@@.A.@@
# @.@@@@..@.
# x@.@@@@.@x
# .@@@@@@@.@
# .@.@.@.@@@
# x.@@@.@@@@
# .@@@@@@@@.
# A.A.@@@.A.

sample = """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""
grid = Grid(sample)


def test_neighbors():
    assert ['.', '@', '@'] == grid.neighbors(0, 0)
    assert ['.', '@', '@', '@', '@'] == grid.neighbors(1, 0)
    assert ['@', '@', '@'] == grid.neighbors(9, 0)
    assert ['.', '.', '@', '@', '@'] == grid.neighbors(0, 1)
    assert ['@', '.', '@', '@', '@'] == grid.neighbors(9, 1)
    assert ['.', '@', '.'] == grid.neighbors(0, 9)
    assert ['.', '@', '@', '@', '@'] == grid.neighbors(1, 9)
    assert ['@', '.', '@'] == grid.neighbors(9, 9)

def test_sample():
    assert 13 == grid.num_accessible()
