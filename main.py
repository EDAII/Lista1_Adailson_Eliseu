from controller import Controller

books = []

while True:
  print('1 - Cadastrar livro;')
  print('2 - Buscar livro por título;')
  print('3 - Buscar livro pelo índice;')
  print('4 - Sair;')
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
    Controller.get_book_by_id(books, id)
  elif op == 4:
    break
  else:
    print('Digite a opção correta!')