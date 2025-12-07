from main import *

sample = """
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +
"""

def test_sample():
    print("")
    print(calculate(sample))

small = """
 79 338  2   956
 84 921  4  2238
562 5154 8  2186
814 6586 39 7546
*   +    +  +
"""

def test_small():
    print("")
    print(calculate(small))
