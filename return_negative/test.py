from main import make_negative


def test_cases():
    assert make_negative(42) == -42
    assert make_negative(-9) == -9
    assert make_negative(0) == 0


if __name__ == "__main__":
    test_cases()