import pytest
from tomerater.TomeRater import NonFiction

@pytest.fixture()
def nonfiction():
    nf = NonFiction("Some non-fiction title", "coding", "beginner", 369258147)
    return nf

def test_CanGetTitleForNonFiction(nonfiction):
    assert nonfiction.get_title() == "Some non-fiction title"

def test_CanGetIsbnForNonFiction(nonfiction):
    assert nonfiction.get_isbn() == 369258147

def test_CanGetSubjectForNonFiction(nonfiction):
    assert nonfiction.get_subject() == "coding"

def test_CanGetLevelForNonFiction(nonfiction):
    assert nonfiction.get_level() == "beginner"

def test_CanGetAverageRatingForNonFiction(nonfiction):
    nonfiction.add_rating(2)
    nonfiction.add_rating(4)
    assert nonfiction.get_average_rating() == 3

def test_CanGetAverageRatingForNonFictionWithNoRatings(nonfiction):
    assert nonfiction.get_average_rating() == 0