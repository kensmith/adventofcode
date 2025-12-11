from main import *

sample = """
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
"""

def test_sample():
    print("")
    f = Factory(sample)
    print(f.adjust())

def test_joltage():
    print("")
    lhs = Joltages([1,2,3,4])
    rhs = Joltages([0,1,0,1])
    assert not lhs == rhs
    new_rhs = Joltages([1,2,3,4])
    assert lhs == new_rhs
    lhs += rhs
    assert "{1,3,3,5}" == str(lhs)
    assert lhs == Joltages([1,3,3,5])
    assert new_rhs < lhs
    assert lhs > new_rhs
    assert new_rhs <= lhs
    assert lhs >= new_rhs
    new_new_rhs = Joltages([1,3,3,5])
    assert lhs <= new_new_rhs
    assert new_new_rhs <= lhs
    lhs = Joltages([1,1,1,1])
    rhs = Joltages([5,2,1,4])
    assert 1 == lhs.closest_index_with_gap(rhs)
    assert [2] == lhs.solved_indices(rhs)
    rhs -= lhs
    assert Joltages([4,1,0,3]) == rhs
    lhs -= rhs
    assert Joltages([-3, 0, 1, -2]) == lhs
    lhs == abs(lhs)
    assert Joltages([3, 0, 1, 2]) == lhs
    assert 66 == int(lhs)

