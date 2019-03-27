from book import Book as books

class Controller():
  def insert_book(title, author):
    return books(title, author)

  # busca sequencial (pelo título)
  def get_book_by_title_seq(books, title):
    count = 0
    for book in books:
      if book.getTitle() == title:
        print('{} | {} | {}'.format(book.getTitle(), book.getAuthor(), book.getId()))
        break
      count += 1

  # busca sequencial (pelo índice)
  def get_book_by_id(books, id):
    count = 0
    for book in books:
      if int(book.getId()) == int(id):
        print('{} | {} | {}'.format(book.getTitle(), book.getAuthor(), book.getId()))
        break
      count += 1

  def get_books(books):
    for book in books:
      print('{} | {} | {}'.format(book.getTitle(), book.getAuthor(), book.getId()))