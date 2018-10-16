from tomerater.TomeRater import Fiction
import pytest

@pytest.fixture()
def fiction():
    f = Fiction("Some fiction title", "Fiction author", 147852369)
    return f

def test_CanGetTitleForFiction(fiction):
    assert fiction.get_title() == "Some fiction title"

def test_CanGetIsbnForFiction(fiction):
    assert fiction.get_isbn() == 147852369

def test_CanGetAuthorForFiction(fiction):
    assert fiction.get_author() == "Fiction author"

def test_CanGetAverageRatingForFiction(fiction):
    fiction.add_rating(2)
    fiction.add_rating(4)
    assert fiction.get_average_rating() == 3

def test_CanGetAverageRatingForBookWithNoRatings(fiction):
    assert fiction.get_average_rating() == 0