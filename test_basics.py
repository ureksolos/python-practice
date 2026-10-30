def test_addition():
    assert 1 + 1 == 2

def test_string_upper():
    assert "hello".upper() == "HELLO"

def test_list_append():
    items = []
    items.append("a")
    assert items == ["a"]