from controller import Controller
from book import Book

books = []

while True:
  print('1 - Cadastrar livro;')
  print('2 - Buscar livro por título;')
  print('3 - Buscar livro pelo índice (sequencial);')
  print('4 - Buscar livro pelo índice (sequencial com sentinela);')
  print('5 - Sair;')
  op = int(input('Entre com a opção desejada: '))
  
  if op == 1:
    title = input('Digite o título:')
    author = input('Digite o autor:')
    books.append(Controller.insert_book(title, author))
  elif op == 2:
    title = input('Digite o título para a pesquisa:')
    Controller.get_book_by_title_seq(books, title)
  elif op == 3:
    id = input('Digite o índice para a pesquisa:')
    Controller.get_book_by_id_seq(books, id)
  elif op == 4:
    id = input('Digite o índice para a pesquisa:')
    title = input('Digite o título:')
    author = input('Digite o autor:')
    books.append(Controller.insert_book(title, author))
    Controller.get_book_by_id_sen(books, id)
  elif op == 5:
    break
  else:
    print('Digite a opção correta!')