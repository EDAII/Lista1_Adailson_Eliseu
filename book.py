import itertools

class Book(object):
  count = itertools.count()
  def __init__(self, title, autor):
    self.__id = next(self.count)
    self.__title = title
    self.__autor = autor

  def getId(self):
    return self.__id
  
  def getTitle(self):
    return self.__title
  
  def getAuthor(self):
    return self.__autor
