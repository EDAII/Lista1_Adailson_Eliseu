import sys  
import os

def main():  

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
   print(len(registers))

main()
