from app.calculations import add


def test_add():
    print("Testing add function...")
    assert add(2, 3) == 5
