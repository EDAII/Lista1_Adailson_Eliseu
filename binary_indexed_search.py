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

# Gera um vetor de indice correspondente ao tamanho da lista de elementos 
def gera_indice(quantidade_numeros, gap_percentage):
    vetor_de_indice = [i*gap_percentage for i in range(quantidade_numeros//gap_percentage)]
    vetor_de_indice.append(quantidade_numeros-1)

    return vetor_de_indice

# Busca binaria em uma lista de elementos
def busca_binaria(lista, valor):
    posicao = -1
    if lista:
        l = 0
        r = len(lista)-1
        if(l<r):
            mid = (l+r)//2
            if(lista[mid] == valor):
                posicao = mid
                posicao_relativa = 0
            elif (lista[mid] < valor):
                posicao_relativa = busca_binaria(lista[mid+1:], valor)
                posicao = mid + 1
            else:
                posicao = l
                posicao_relativa = busca_binaria(lista[:mid], valor)

            if(posicao_relativa != -1):
                posicao = posicao + posicao_relativa
            else:
                posicao = -1
        elif lista[0] == valor:
            posicao = 0
    return posicao

# Busca sequencial no indice da lista 
def busca_no_indice(indice, lista, valor):
    indice_fim = len(indice)-1
    posicao = -1
    intervalo = [
        indice[0],
        indice[indice_fim]
        ]
    if indice and lista:
        if lista[indice[0]] <= valor and lista[indice[indice_fim]] >= valor:
            for i in range (indice_fim+1):
                if lista[indice[i]] > valor:
                    intervalo = [
                        indice[i-1],
                        indice[i]
                        ]
                    break;
            print("Inicio do Intervalo", intervalo[0], "Fim do Intervalo", intervalo[1])
            posicao_relativa = busca_binaria(lista[intervalo[0]:intervalo[1]], valor)
            if not(posicao_relativa == -1):
                posicao = intervalo[0] + posicao_relativa
        elif lista[indice[indice_fim]] == valor:
            posicao = indice[indice_fim]

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
    vetor_de_indice = gera_indice(quantidade_numeros, gap_percentage)
    print(vetor_de_indice, "Tamanho indice", len(vetor_de_indice))
    n = input("")
    start = time.time()
    value = int(n)
    posicao = busca_no_indice(vetor_de_indice, lista_de_valores, value)
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
    vetor_de_indice = gera_indice(quantidade_numeros, gap_percentage)
    total_time = 0
    for n in range(quantidade_buscas):
        start = time.time()
        value = int(lista_de_valores[int(n*len(lista_de_valores)/quantidade_buscas)])
        posicao = busca_no_indice(vetor_de_indice, lista_de_valores, value)
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
    quantidade_numeros = 200000000
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