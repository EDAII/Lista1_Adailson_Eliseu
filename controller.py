from book import Book as books

class Controller():
  def insert_book(title, author):
    return books(title, author)

  # busca sequencial
  def get_book_by_title_seq(books, title):
    count = 0
    for book in books:
      if book.getTitle() == title:
        print('{} | {}'.format(book.getTitle(), book.getAuthor()))
        break
      count += 1