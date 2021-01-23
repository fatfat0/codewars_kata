from main import toCsvText

array = [
    [0, 1, 2, 3, 4],
    [10, 11, 12, 13, 14],
    [20, 21, 22, 23, 24],
    [30, 31, 32, 33, 34],
]


def test_toCsvText(array):
    result = "0,1,2,3,4\n" + "10,11,12,13,14\n" + "20,21,22,23,24\n" + "30,31,32,33,34"
    assert toCsvText(array) == result


if __name__ == "__main__":
    test_toCsvText(array)
