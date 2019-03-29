import math

def sort_by_time(data):
    return data[0]

def get_estimate_data_shape(number_of_register):

    fields_per_register = 4
    max_size_in_memory = fields_per_register*5000100 # for 8 GB+ RAM
    best_cs = []
    data_spin_range = 10
    min_index_size = 10
    max_index_size = int(number_of_register/5000)
    for i in range(min_index_size, max_index_size, data_spin_range):
        index_size = i
        chunk_size = int(number_of_register/index_size) + 1
        if(max_size_in_memory > (2*index_size + fields_per_register*chunk_size)):
            best_cs.append([int(math.log(index_size, 2) * (math.log(chunk_size, 2) + chunk_size)), (2*index_size + fields_per_register*chunk_size), index_size, chunk_size])
    best_cs.sort(key=sort_by_time)
    return best_cs[0][2:]

def main():
    index_size, chunk_size = get_estimate_data_shape(850000000)
    print("index_size\tchunk_size")
    print("{}\t\t{}".format(index_size, chunk_size))
    print("Possibilities: {}".format(index_size * chunk_size))


if __name__ == '__main__':
    main()