class Book():
  def __init__(self, title, autor):
    self.__title = title
    self.__autor = autor

  def getTitle(self):
    return self.__title
  
  def getAuthor(self):
    return self.__autor
