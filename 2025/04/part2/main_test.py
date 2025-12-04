from main import *

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


def test_neighbors():
    print("")
    grid = Grid(sample)
    assert ['.', '@', '@'] == grid.neighbors(0, 0)
    assert ['.', '@', '@', '@', '@'] == grid.neighbors(1, 0)
    assert ['@', '@', '@'] == grid.neighbors(9, 0)
    assert ['.', '.', '@', '@', '@'] == grid.neighbors(0, 1)
    assert ['@', '.', '@', '@', '@'] == grid.neighbors(9, 1)
    assert ['.', '@', '.'] == grid.neighbors(0, 9)
    assert ['.', '@', '@', '@', '@'] == grid.neighbors(1, 9)
    assert ['@', '.', '@'] == grid.neighbors(9, 9)

def test_sample():
    print("")
    grid = Grid(sample)
    assert 13 == len(grid.accessible_paper())

def test_remove_some():
    print("")
    grid = Grid(sample)

    assert """
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
""".strip() == str(grid).strip()

    grid.remove_accessible_paper()

    assert """
.......@..
.@@.@.@.@@
@@@@@...@@
@.@@@@..@.
.@.@@@@.@.
.@@@@@@@.@
.@.@.@.@@@
..@@@.@@@@
.@@@@@@@@.
....@@@...
""".strip() == str(grid).strip()

    grid.remove_accessible_paper()

    assert """
..........
.@@.....@.
.@@@@...@@
..@@@@....
.@.@@@@...
..@@@@@@..
...@.@.@@@
..@@@.@@@@
..@@@@@@@.
....@@@...
""".strip() == str(grid).strip()

    grid.remove_accessible_paper()

    assert """
..........
..@.......
.@@@@.....
..@@@@....
...@@@@...
..@@@@@@..
...@.@.@@.
..@@@.@@@@
...@@@@@@.
....@@@...
""".strip() == str(grid).strip()

    grid.remove_accessible_paper()

    assert """
..........
..........
..@@@.....
..@@@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@@.
....@@@...
""".strip() == str(grid).strip()

    grid.remove_accessible_paper()

    assert """
..........
..........
...@@.....
..@@@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@..
....@@@...
""".strip() == str(grid).strip()

    grid.remove_accessible_paper()

    assert """
..........
..........
...@@.....
...@@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@..
....@@@...
""".strip() == str(grid).strip()

    grid.remove_accessible_paper()

    assert """
..........
..........
....@.....
...@@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@..
....@@@...
""".strip() == str(grid).strip()

    grid.remove_accessible_paper()

    assert """
..........
..........
..........
...@@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@..
....@@@...
""".strip() == str(grid).strip()

    grid.remove_accessible_paper()

    assert """
..........
..........
..........
....@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@..
....@@@...
""".strip() == str(grid).strip()

def test_remove_all():
    grid = Grid(sample)
    total = grid.remove_all_paper()
    assert 43 == total
