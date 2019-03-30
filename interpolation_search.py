import numpy as np
import sys
import time
from math import sqrt

# Gera uma lista de (quantidade_numeros) numeros de elementos
# Os numeros gerados estao contidos no intervalo [limite_inferior, limite_superior]
def gera_lista(limite_inferior, limite_superior, quantidade_numeros):
    lista_de_valores = list(
        np.linspace(limite_inferior, limite_superior, num=quantidade_numeros, endpoint=False, dtype=int)
    )
    return lista_de_valores

# Busca interpolação em uma lista de elementos
def busca_interpolacao(lista, valor):
    posicao = -1
    lista = gera_lista(limite_inferior, limite_superior, quantidade_numeros)
    begin = 0
    end = len(lista) - 1
    while begin <= end and lista[begin] <= valor <= lista[end]:
        i = int(begin + (((end - begin)/(lista[end] - lista[begin])) * (valor - lista[begin])))
        if lista[i] == valor:
            posicao = i
            break
        if valor > lista[i]:
            begin = i + 1
        else:
            end = i - 1
    return posicao

def abs_time_with_precision(number, fraction_digits=2, is_ms=False):
    if is_ms:
        ms_convertion = 1
    else:
        ms_convertion = 1000
    return int(number*ms_convertion*(10**fraction_digits))/(10**fraction_digits)


# Busca um elemento na lista de elementos
def main(quantidade_numeros, gap_percentage):
    print('Digite o valor que deseja procurar no vetor: \n')
    lista_de_valores = gera_lista(limite_inferior, limite_superior, quantidade_numeros)
    n = input("")
    start = time.time()
    value = int(n)
    posicao = busca_interpolacao(lista_de_valores, value)
    if posicao >= 0:
        print("O valor esta localizado na posicao: ", posicao)
        print("O valor {} bate com o valor {}.".format(n, lista_de_valores[posicao]))
    else:
        print("valor nao encontrado")
    end = time.time()
    total_time = (end - start)
    print("Tempo de resposta: ", abs_time_with_precision(total_time, 4), "ms")

# Executa uma busca para cada elemento na lista_de_valores
def performance(quantidade_numeros, gap_percentage):
    quantidade_buscas = 1000
    print("Buscando {} elementos em {} de elementos...".format(quantidade_buscas, quantidade_numeros))
    lista_de_valores = gera_lista(limite_inferior, limite_superior, quantidade_numeros)
    total_time = 0
    for n in range(quantidade_buscas):
        start = time.time()
        value = int(lista_de_valores[int(n*len(lista_de_valores)/quantidade_buscas)])
        posicao = busca_interpolacao(lista_de_valores, value)
        if posicao >= 0:
            pass
        else:
            pass
        end = time.time()
        total_time = total_time + (end - start)

    print("Tempo de resposta: ", abs_time_with_precision(total_time, 4, True), "s")
    print("Tempo médio de resposta: ", abs_time_with_precision(total_time/quantidade_buscas, 4), "ms")

if __name__ == '__main__':

    n = int(input('0 - Performance Automatica\n1 - Busca Manual: \n'))
    quantidade_numeros = 2000
    print("Quantidade de elementos", quantidade_numeros)
    gap_percentage = int(quantidade_numeros*0.05)
    # parametros do algoritmo
    limite_inferior = 0
    limite_superior = quantidade_numeros*10
    
    if n:
        main(quantidade_numeros, gap_percentage)
    else:
        performance(quantidade_numeros, gap_percentage)
    exit()