import pytest
from main import *

# 11-22 has two invalid IDs, 11 and 22.
# 95-115 has one invalid ID, 99.
# 998-1012 has one invalid ID, 1010.
# 1188511880-1188511890 has one invalid ID, 1188511885.
# 222220-222224 has one invalid ID, 222222.
# 1698522-1698528 contains no invalid IDs.
# 446443-446449 has one invalid ID, 446446.
# 38593856-38593862 has one invalid ID, 38593859.
# The rest of the ranges contain no invalid IDs.
# Adding up all the invalid IDs in this example produces 1227775554.

# 11, 22, 2, 2, 1, 1
# 95, 115, 2, 3, 1, 2
# 998, 1012, 3, 4, 2, 2
# 1188511880, 1188511890, 10, 10, 5, 5
# 222220, 222224, 6, 6, 3, 3
# 446443, 446449, 6, 6, 3, 3
# 38593856, 38593862, 8, 8, 4, 4
# 565653, 565659, 6, 6, 3, 3
# 2121212118, 2121212124, 10, 10, 5, 5


def test_example():
    print("")
    assert set() == invalid_ids(1698522, 1698528) # []
    assert {824824824} == invalid_ids(824824821, 824824827) # []
    assert {11, 22} == invalid_ids(11, 22) # [11, 22]
    assert {99, 111} == invalid_ids(95, 115) # [99]
    assert {999, 1010} == invalid_ids(998, 1012) # [1010]
    assert {1188511885} == invalid_ids(1188511880, 1188511890) # 1188511885
    assert {222222} == invalid_ids(222220, 222224) # 222222
    assert {446446} == invalid_ids(446443, 446449) # [446446]
    assert {38593859} == invalid_ids(38593856, 38593862) # 38593859
    assert {565656} == invalid_ids(565653, 565659) # []
    assert {2121212121} == invalid_ids(2121212118, 2121212124) # []
