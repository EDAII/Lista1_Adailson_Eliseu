import itertools

class Book(object):
  count = itertools.count()
  def __init__(self, title, author):
    self.__id = next(self.count)
    self.__title = title
    self.__author = author
    
  def getId(self):
    return self.__id
  
  def getTitle(self):
    return self.__title
  
  def getAuthor(self):
    return self.__author
