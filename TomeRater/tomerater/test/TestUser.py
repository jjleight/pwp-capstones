import pytest
from tomerater.TomeRater import User

@pytest.fixture()
def user():
    u = User("Bob", "bob@bobson.co.uk")
    return u

def test_CanGetEmailForUser(user):
    assert user.get_email() == "bob@bobson.co.uk"

def test_CanChangeEmailForUser(user):
    user.change_email("bobby@bobson.co.uk")
    assert user.get_email() == "bobby@bobson.co.uk"

def test_CanReadBookWithNoRatingForUser(user):
    book = "Bob vs the world"
    user.read_book(book)
    assert user.books[book] is None

def test_CanReadBookWithRatingForUser(user):
    book = "Bob vs the world"
    user.read_book(book, 4)
    assert user.books[book] == 4

def test_CanGetAverageRatingForUser(user):
    book = "Bob vs the world"
    book2 = "Another book"
    user.read_book(book, 4)
    user.read_book(book2, 2)
    assert user.get_average_rating() == 3

def test_CanGetAverageRatingForUserWhenNoRatings(user):
    assert user.get_average_rating() == 0