class Library:

  def __init__(self):
    self.noBooks = 0
    self.books = []

  def addBooks(self, book):
    self.books.append(book)
    self.noBooks = len(self.books)

  def buyBooks(self, book):
    isAvailable = True
    for b in self.books:
      if(book == b):
        isAvailable = True
      else:
        isAvailable = False

    if(isAvailable):
      print(f"Yes the {book} is available")
    else:
      print(f"Sorry the {book} is not available")

  def showInfo(self):
    print(f"The library has {self.noBooks} books. The books are")
    for book in self.books:
      print(book)

l1 = Library()
l1.addBooks("To Kill a Mockingbird")
l1.addBooks("And Then There Were None")
l1.addBooks("Educated")
l1.addBooks("Jane Eyre")
l1.addBooks("Les Misérables")
l1.showInfo()
l1.buyBooks("Les Misérables")