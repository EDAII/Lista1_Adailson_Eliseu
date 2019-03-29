import linecache
import sys

def transfer_data(arquivo_origem, arquivo_destino):
    with open(arquivo_destino, "a+") as destino:
        invalid_position = 0
        line_index = 1
        block_size = 1000
        while(line_index != invalid_position):
            for block_index in range(block_size):
                line = linecache.getline(arquivo_origem, line_index)
                if (line):
                    destino.write(line)
                    line_index = 1 + line_index
                else:
                    line_index = invalid_position
                    break
            linecache.clearcache()

if __name__ == '__main__':
    if(len(sys.argv) == 3):
        print("Iniciando transferência de dados de {} para {}".format(sys.argv[1], sys.argv[2]))
    else:
        print("    Usage: python3 {} origin_text_file destiny_text_file\n".format(sys.argv[0]))
    exit()