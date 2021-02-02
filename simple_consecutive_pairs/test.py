from main import pairs
from main import pairs_2


def test_cases():
    assert pairs_2([1, 2, 5, 8, -4, -3, 7, 6, 5]) == 3
    assert pairs_2([21, 20, 22, 40, 39, -56, 30, -55, 95, 94]) == 2
    assert pairs_2([81, 44, 80, 26, 12, 27, -34, 37, -35]) == 0
    assert pairs_2([-55, -56, -7, -6, 56, 55, 63, 62]) == 4
    assert pairs_2([73, 72, 8, 9, 73, 72]) == 3


if __name__ == "__main__":
    test_cases()