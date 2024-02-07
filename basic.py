

def split_file(file, k):
    with open(file, 'r') as file:
        lines = file.readlines()
    
    # the size defined by the number of chunks
    chunkSize = len(lines) // k
    for i in range(k):
        with open(f'chunk_of_{k}_{i+1}.txt', 'w') as chunk_file:
            if i < k - 1:
                # write the lines to the current chunk
                chunk_file.writelines(lines[i*chunkSize:(i+1)*chunkSize])
            else:
                # last chunk contains all remaining lines
                chunk_file.writelines(lines[i*chunkSize:])


input_str = input("Enter an integer: ")
noOfChunks = int(input_str)

split_file('network.txt', noOfChunks)