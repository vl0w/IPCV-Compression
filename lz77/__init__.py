def encode(input_data, buffer_size, lookahead_bufsize):
    def get_buffer(index) -> str:
        index_from = index - buffer_size

        index_to = index_from + buffer_size

        if index_from < 0:
            index_from = 0

        buffer = input_data[index_from:index_to]
        return buffer

    def get_lookahead_buffer(index):
        return input_data[index:index + lookahead_bufsize]

    global_index = 0
    encoded_triples = []

    while global_index < len(input_data):
        lookahead_buffer = get_lookahead_buffer(global_index)
        buffer = get_buffer(global_index)

        last_found_triple = [0, 0, None]
        lookahead_index = 0
        search_string = ""
        for lookahead_index in range(1, len(lookahead_buffer) + 1):
            search_string = lookahead_buffer[:lookahead_index]
            if search_string in buffer:
                string_found_in_buffer_at_index = buffer.index(search_string) + 1 - len(buffer) + buffer_size
                last_found_triple[0] = string_found_in_buffer_at_index
                last_found_triple[1] = lookahead_index
            else:
                break
        if lookahead_index < len(lookahead_buffer):
            last_found_triple[2] = search_string[-1:]
        encoded_triples.append(last_found_triple)
        global_index += lookahead_index


    result = []
    for triple in encoded_triples:
        result.append(triple[0])
        result.append(triple[1])
        result.append(triple[2])

    return result
