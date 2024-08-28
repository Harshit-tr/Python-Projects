class Library:
  def __init__(self):
    self.noBooks = 0
    self.Books = []

  def Addbooks(self,book):
    self.Books.append(book)
    self.noBooks = len(self.Books)

  def showInfo(self):
    if len(self.Books)==0:
      print("No books are present in the library")
    else:  
     print(f"The library has {self.noBooks} books. The books are")
     for book in self.Books:
       print(book)

l1 = Library()
# Add books in a loop
while True:
    book = input("Enter the name of the book to add (or type 'done' to finish): ")
    if book.lower() == 'done':
        break
    l1.Addbooks(book)
# Show the information  
l1.showInfo()