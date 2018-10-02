class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}
    
    def __repr__(self):
        return "User {name}, email: {email}, books read: {books_read}".format(name=self.name, email=self.email, books_read=len(self.books))

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
        	return True
        else:
        	return False

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("Your email address has been updated.")
        
    def read_book(self, book, rating=None):
    	self.books[book] = rating
    	
    def get_average_rating(self):
    	total = 0
    	for book, rating in self.books.items():
    		if rating != None:
    			total += rating
    	return total/len(self.books)
        	
class Book(object):
	def __init__(self, title, isbn):
		self.title = title
		self.isbn = isbn
		self.ratings = []
	
	def __repr__(self):
		return "{title}".format(title=self.title)
	
	def __eq__(self, other_book):
		if self.title == other_book.title and self.isbn == other_book.isbn:
			return True
		else:
			return False
	
	def __hash__(self):
		return hash((self.title, self.isbn))
	
	def get_title(self):
		return self.title
	
	def get_isbn(self):
		return self.isbn
		
	def set_isbn(self, new_isbn):
		self.isbn = new_isbn
		print("{book}: ISBN has been updated.".format(book=self.title))
		
	def add_rating(self, rating):
		if rating != None:
			if rating >= 0 and rating <= 4:
				self.ratings.append(rating)
			else:
				print("Invalid Rating")

	def get_average_rating(self):
		total = 0
		for rating in self.ratings:
			total += rating
		return total/len(self.ratings)
			
class Fiction(Book):
	def __init__(self, title, author, isbn):
		super().__init__(title, isbn)
		self.author = author
		
	def __repr__(self):
		return "{title} by {author}".format(title=self.title, author=self.author)
		
	def get_author(self):
		return self.author
		
class Non_Fiction(Book):
	def __init__(self, title, subject, level, isbn):
		super().__init__(title, isbn)
		self.subject = subject
		self.level = level
	
	def __repr__(self):
		return "{title}, a {level} manual on {subject}".format(title=self.title, level=self.level, subject=self.subject)
		
	def get_subject(self):
		return self.subject
		
	def get_level(self):
		return self.level
		
class TomeRater:
	def __init__(self):
		self.users = {}
		self.books = {}
	
	def __repr__(self):
		return "Current users: {users}; Current books: {books}".format(users=self.users, books=self.books)
		
	def create_book(self, title, isbn):
		return Book(title, isbn)
		
	def create_novel(self, title, author, isbn):
		return Fiction(title, author, isbn)
		
	def create_non_fiction(self, title, subject, level, isbn):
		return Non_Fiction(title, subject, level, isbn)
		
	def add_book_to_user(self, book, email, rating=None):
		if email in self.users:
			self.users[email].read_book(book, rating)
			book.add_rating(rating)
		else:
			print("No user with email {email}!".format(email=email))
		if book in self.books:
			self.books[book] += 1
		else:
			self.books[book] = 1
	
	def add_user(self, name, email, user_books=None):
		valid_email_check = ["@", ".com", ".org", ".edu", ".co.uk"]
		valid_email = 0
		for item in valid_email_check:
			if item in email:
				valid_email += 1
		if valid_email >= 2:
			if email not in self.users:
				self.users[email] = User(name, email)
				if user_books != None:
					for book in user_books:
						self.add_book_to_user(book, email)
			else:
				print("There is already a user with email: {email}, please try adding a new user.".format(email=email))
		else:
			print("You've not entered a valid email address, please check!")

	def print_catalog(self):
		for book in self.books.keys():
			print(book.title)
	
	def print_users(self):
		for user in self.users.keys():
			user.__repr__()
	
	def most_read_book(self):
		highest_count = 0
		most_read_book = ""
		for book, times_read in self.books.items():
			if times_read > highest_count:
				highest_count = times_read
				most_read_book = book.get_title()
		return most_read_book
	
	def get_n_most_read_books(self, n):
		sorted_books = sorted(self.books, key=self.books.__getitem__, reverse=True)
		return sorted_books[:n-1]
	
	def highest_rated_book(self):
		highest_avg_rating = 0
		highest_avg_rated_book = ""
		for book in self.books.keys():
			avg_rating = book.get_average_rating()
			if avg_rating > highest_avg_rating:
				highest_avg_rating = avg_rating
				highest_avg_rated_book = book.get_title()
		return highest_avg_rated_book
	
	def most_positive_user(self):
		highest_avg_rating = 0
		most_positive_user = ""
		for email, user in self.users.items():
			avg_rating = user.get_average_rating()
			if avg_rating > highest_avg_rating:
				highest_avg_rating = avg_rating
				most_positive_user = user.name
		return most_positive_user
