from books_13 import format_book

def test_format_book_no_year():
    assert format_book("Brain", "Tim Cook", None) == "Brain — Tim Cook"

def test_format_book_with_year():
    assert format_book("Brain", "Tim Cook", 2024) == "Brain — Tim Cook (2024)"

def test_format_book_with_empty_author():
    assert format_book("Brain", "", 2024) == "Brain —  (2024)"