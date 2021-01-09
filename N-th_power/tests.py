from main import index


def test_1():
    array = [1, 2, 3, 4]
    N = 2

    assert index(array, N) == 9


def test_2():
    array = [1, 2, 3]
    N = 3

    assert index(array, N) == -1


if __name__ == "__main__":
    test_1()
    test_2()
