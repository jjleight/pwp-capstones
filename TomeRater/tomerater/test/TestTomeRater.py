from tomerater.TomeRater import TomeRater, Fiction, Book, NonFiction, User


def test_CanCreateBookForTomeRater():
    tr = TomeRater()
    book1 = tr.create_book("Book 1", 123456)
    assert book1 == Book("Book 1", 123456)

def test_CanCreateNovelForTomeRater():
    tr = TomeRater()
    novel1 = tr.create_novel("Novel 1", "Some Author", 741852)
    assert novel1 == Fiction("Novel 1", "Some Author", 741852)

def test_CanCreateNonFictionForTomeRater():
    tr = TomeRater()
    nonfiction1 = tr.create_non_fiction("Non-fiction 1", "non-fiction subject", "non-fiction level", 987654)
    assert nonfiction1 == NonFiction("Non-fiction 1", "non-fiction subject", "non-fiction level", 987654)

def test_CanAddNewUserWithNoBooksForTomeRater():
    tr = TomeRater()
    tr.add_user("Bob Bobson", "bob@bobson.co.uk")
    assert tr.users["bob@bobson.co.uk"] == User("Bob Bobson", "bob@bobson.co.uk")