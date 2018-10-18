import pytest
from tomerater.TomeRater import Book

@pytest.fixture()
def book():
    b = Book("Some book", 12324235)
    return b

def test_CanGetTitleForBook(book):
    assert book.get_title() == "Some book"

def test_CanGetIsbnForBook(book):
    assert book.get_isbn() == 12324235

def test_CanSetIsbnForBook(book):
    book.set_isbn(987654321)
    assert book.get_isbn() == 987654321

def test_CanGetAverageRatingForBook(book):
    book.add_rating(2)
    book.add_rating(4)
    assert book.get_average_rating() == 3

def test_CanGetAverageRatingForBookWithNoRatings(book):
    assert book.get_average_rating() == 0