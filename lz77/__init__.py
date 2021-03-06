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
                string_found_in_buffer_at_index = buffer.rfind(search_string) + 1 - len(buffer) + buffer_size
                last_found_triple[0] = string_found_in_buffer_at_index
                last_found_triple[1] = lookahead_index
            else:
                break

        last_not_found_character = search_string[-1:]
        if lookahead_index < len(lookahead_buffer) or last_not_found_character not in buffer:
            last_found_triple[2] = search_string[-1:]

        encoded_triples.append(last_found_triple)
        global_index += lookahead_index

    result = []
    for triple in encoded_triples:
        result.append(triple[0])
        result.append(triple[1])
        result.append(triple[2])

    return result


def decode(input_data, bufsize):
    triples = grouped(input_data, 3)
    result = ""

    for item_index, item_amount, char in triples:
        if item_index > 0:
            n = (item_index - bufsize - 1)
            new_chars = (result[n:])[:item_amount]
            result += new_chars

        if char is not None:
            result += char

    return result


def grouped(iterable, n):
    "s -> (s0,s1,s2,...sn-1), (sn,sn+1,sn+2,...s2n-1), (s2n,s2n+1,s2n+2,...s3n-1), ..."
    return list(zip(*[iter(iterable)] * n))
