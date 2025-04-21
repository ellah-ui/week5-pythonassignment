class Book:
    def __init__(self, title, genre, pages):
        self.title = title
        self.genre = genre
        self.pages = pages
    
    def get_info(self):
        return f"Title: '{self.title}', Genre: {self.genre}, {self.pages} pages long"

# Demonstrates inheritance and polymorphism
class EBook(Book):
    def __init__(self, title, genre, pages, author):
        super().__init__(title, genre, pages)
        self.author = author
    
    def get_info(self):
        return f"Title: {self.title}, Genre: {self.genre}, {self.pages} pages, by {self.author}"

#Example usage
book1 = Book("The Great Gatsby", "Fiction", 180)
book2 = EBook("Digital Fortress", "Thriller", 384, "Dan Brown")

print(book1.get_info())
print(book2.get_info())