import json
import random
import sys


def gera_lista(limite_inferior, limite_superior, quantidade_numeros):
    lista_de_valores = []
    for i in range(limite_inferior, limite_superior, (limite_superior - limite_inferior)//quantidade_numeros):
        lista_de_valores.append(
            '"{:011d}", "{}", "{}", "{}"\n'.format(
                i,
                names[random.randint(0,quantidade_names-1)],
                middle_names[random.randint(0,quantidade_middle_names-1)],
                surnames[random.randint(0,quantidade_surnames-1)]
                )
            )
    return lista_de_valores

def gera_arquivo(limite_inferior, limite_superior, quantidade_numeros, arquivo):
    lista_de_valores = []
    with open(arquivo, "w+") as file:
        for i in range(limite_inferior, limite_superior, (limite_superior - limite_inferior)//quantidade_numeros):
            file.write(
                '"{:011d}", "{}", "{}", "{}"\n'.format(
                    i,
                    names[random.randint(0,quantidade_names-1)],
                    middle_names[random.randint(0,quantidade_middle_names-1)],
                    surnames[random.randint(0,quantidade_surnames-1)]
                    )
                )

def load_names(filename):
    names = []
    with open(filename) as json_file:  
        data = json.load(json_file)
        names = [p for p in data]
    return names

if __name__ == '__main__':

    if len(sys.argv) == 4:
        filename = sys.argv[1]
        quantidade_arquivos = sys.argv[2]
        quantidade_numeros = sys.argv[3]
    else:
        filename = "registered{}.csv"
        quantidade_arquivos = 1
        quantidade_numeros = 50000000

    # parametros do algoritmo
    names = load_names('names.json')
    quantidade_names = len(names)
    middle_names = load_names('middle-names.json')
    quantidade_middle_names = len(middle_names)
    surnames = load_names('surnames.json')
    quantidade_surnames = len(surnames)

    # ALTERAR os arquivos gerados são definidos aqui
    for i in range(quantidade_arquivos):
        limite_inferior = 0 + i*quantidade_numeros
        limite_superior = quantidade_numeros + i*quantidade_numeros
        gera_arquivo(limite_inferior, limite_superior, quantidade_numeros, filename.format(i))
