from main import solve


def test_cases():
    assert solve(0, 10) == 3
    assert solve(10, 100) == 4
    assert solve(100, 1000) == 12
    assert solve(1000, 10000) == 20
    assert solve(10000, 15000) == 6
    assert solve(15000, 20000) == 9
    assert solve(60000, 70000) == 15
    assert solve(60000, 130000) == 55


if __name__ == "__main__":
    test_cases()