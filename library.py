class Library:
  def __init__(self):
    self.noOfBooks=0
    self.books=[]
  
  def addBooks(self,book):
    self.books.append(book)
    self.noOfBooks=len(self.books)
    
  def showinfo(self):
    print(f"The Library has {self.noOfBooks} Books.The Books are")
    for book in self.books:
      print(book)  
    
li=Library()
li.addBooks("DSA")    
li.addBooks("Java")
li.addBooks("Operating System")    
li.showinfo()