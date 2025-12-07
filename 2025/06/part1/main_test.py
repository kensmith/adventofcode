from main import *

sample = """
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +
"""

def test_sample():
    print("")
    assert 4277556 == calculate(sample)
