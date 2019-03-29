import sys  
import os

class Register:
    def __init__(self, register): 
        self.register = register

    def store_file(self): 
        # Csv que contém 5 milhões de registros, necessário leitura linha a linha para não
        # haver estouro de memória 
        filepath = 'registered0.csv'
        registers = []
        if not os.path.isfile(filepath):
            print("O Arquivo {} não foi encontrado.".format(filepath))
            sys.exit()
       
        with open(filepath) as fp:
            cnt = 0
            for line in fp:
                registers.append(line)
                #print("Linha {} contém {}".format(cnt, line))
                cnt += 1
        return registers

    def interpolation_search(self):
        
        vector = self.store_file()
        vector = [v[0] for v in vector]
        first = vector.pop(0)
        vector = [int(v[0]) for v in vector]
        
        begin = 0
        end = len(vector) - 1
        while begin <= end and vector[begin] <= self.valor_a_ser_encontrado <= vector[end]:
            i = int(begin + (((end - begin)/(vector[end] - vector[begin])) * (self.valor_a_ser_encontrado - vector[begin])))
            if vector[i] == self.valor_a_ser_encontrado:
                return "O elemento {} foi encontrado na posição {}".format(self.valor_a_ser_encontrado, i)

            if self.valor_a_ser_encontrado > vector[i]:
                begin = i + 1

            else:
                end = i - 1

register = Register('00000057283')
number = register.interpolation_search()
print(number)