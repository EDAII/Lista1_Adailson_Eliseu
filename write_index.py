import pandas as pd
import sys

file_size = 50000000
index_file = "index.csv"

def get_data_from_file(filename, chunk_size, chunk_index=0):
    data = []
    chunks = pd.read_csv(filename, skiprows=chunk_index*chunk_size, chunksize=chunk_size)
    for chunk in chunks:
        data = chunk.values.tolist()
        break
            
    return data

def write_index(filename, chunk_size):
    data = []
    with open(index_file, "w+") as file:
        file.write('"filepath", "position", "data"\n')
    body_index = []
    for i in range(file_size//chunk_size):
        data = get_data_from_file(filename, chunk_size, i)
        body_index.append('"{}", "{}", "{:011d}"\n'.format(filename, i*chunk_size, data[0][0]))
    with open(index_file, "a+") as file:
        file.write(body_index)
        file.write('"{}", "{}", "{:011d}"\n'.format(filename, file_size-1, data[-1][0]))

def main():
    if (len(sys.argv)>2):
        file_index = sys.argv[1]
        chunk_size = int(sys.argv[2])
        filename_template = "data/registered{}.csv"
        filename = filename_template.format(file_index)
        write_index(filename, chunk_size)
    else:
        print("Missing argument...")
        print("USAGE:\t{} filename chunk_size".format(sys.argv[0]))


if __name__ == '__main__':
    main()