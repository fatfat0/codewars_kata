from main import triangle


def test_cases():
    assert triangle("GB") == "R"
    assert triangle("RRR") == "R"
    assert triangle("RGBG") == "B"
    assert triangle("RBRGBRB") == "G"
    assert triangle("RBRGBRBGGRRRBGBBBGG") == "G"
    assert triangle("B") == "B"


if __name__ == "__main__":
    test_cases()