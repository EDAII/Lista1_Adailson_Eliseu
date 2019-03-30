import pandas as pd

file_size = 50000000

filename = "registered0.csv"

chunk_size = file_size//10

data = [] 
chunks = pd.read_csv(filename, chunksize=chunk_size)
for chunk in chunks:
    data = chunk
    break
