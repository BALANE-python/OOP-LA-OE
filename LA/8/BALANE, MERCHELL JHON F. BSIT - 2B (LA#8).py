class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
print(book1.title, book1.author)

del book1.author


book2 = Book("Moby Dick", "Herman Melville")
print(book2.author)
