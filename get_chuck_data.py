import pandas as pd

file_size = 50000000

filename = "registered16.csv"

chunk_size = file_size//10

data = [] 
chunk_index = 4
chunks = pd.read_csv(filename, skiprows=chunk_index*chunk_size, chunksize=chunk_size)
for chunk in chunks:
    data = chunk
    break
