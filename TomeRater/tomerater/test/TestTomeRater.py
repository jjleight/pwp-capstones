import pytest
from tomerater.TomeRater import TomeRater, Fiction, Book, NonFiction, User

@pytest.fixture()
def tomerater():
    tr = TomeRater()
    return tr

def test_CanCreateBookForTomeRater(tomerater):
    book1 = tomerater.create_book("Book 1", 123456)
    assert book1 == Book("Book 1", 123456)

def test_CanCreateNovelForTomeRater(tomerater):
    novel1 = tomerater.create_novel("Novel 1", "Some Author", 741852)
    assert novel1 == Fiction("Novel 1", "Some Author", 741852)

def test_CanCreateNonFictionForTomeRater(tomerater):
    nonfiction1 = tomerater.create_non_fiction("Non-fiction 1", "non-fiction subject", "non-fiction level", 987654)
    assert nonfiction1 == NonFiction("Non-fiction 1", "non-fiction subject", "non-fiction level", 987654)

def test_CanAddNewUserWithNoBooksForTomeRater(tomerater):
    tomerater.add_user("Bob Bobson", "bob@bobson.co.uk")
    assert tomerater.users["bob@bobson.co.uk"] == User("Bob Bobson", "bob@bobson.co.uk")

def test_CanAddUserWithBooksForTomeRater(tomerater):
    book1 = tomerater.create_book("Book 1", 123456)
    book2 = tomerater.create_book("Book 1", 654321)
    book3 = tomerater.create_book("Book 1", 147852)
    tomerater.add_user("Bob Bobson", "bob@bobson.co.uk", [book1, book2, book3])
    assert tomerater.users["bob@bobson.co.uk"] == User("Bob Bobson", "bob@bobson.co.uk")
    assert tomerater.books == {book1: 1, book2: 1, book3: 1}

def test_CannotAddUserWithExistingEmailForTomeRater(tomerater, capsys):
    tomerater.add_user("Bob Bobson", "bob@bobson.co.uk")
    tomerater.add_user("Bob Bobson", "bob@bobson.co.uk")
    captured = capsys.readouterr()
    assert tomerater.users["bob@bobson.co.uk"] == User("Bob Bobson", "bob@bobson.co.uk")
    assert captured.out == "There is already a user with email: bob@bobson.co.uk, please try adding a new user.\n"

def test_CannotAddUserWithInvalidEmailForTomeRater(tomerater, capsys):
    tomerater.add_user("Bob Bobson", ".com@.co.uk.not.a.real.email_:)")
    tomerater.add_user("Bob Bobson", "bob@bob@bob.co.uk")
    tomerater.add_user("Bob Bobson", "bob@.com.co.uk")
    tomerater.add_user("Bob Bobson", "bobby&johnson.co.uk")
    captured = capsys.readouterr()
    assert captured.out == "You've not entered a valid email address, please check!\nYou've not entered a valid email address, please check!\nYou've not entered a valid email address, please check!\nYou've not entered a valid email address, please check!\n"
    assert tomerater.users == {}