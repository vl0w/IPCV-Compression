import copy


def encode(input_data, dictionary=["a", "b", "c"]):
    pass


basic_dictionary = ["a", "b", "c"]


def decode(input_data):
    dictionary = copy.copy(basic_dictionary)
    dictionary.insert(0, None)

    result_entries = []
    for next_index in input_data:
        if next_index >= len(dictionary):
            new_entry = ''.join([result_entries[-1], (result_entries[-1])[0]])
            dictionary.append(new_entry)
            result_entries.append(new_entry)
        else:
            result_entries.append(dictionary[next_index])
            if len(result_entries) > 1:
                dictionary.append(''.join([result_entries[-2], (result_entries[-1])[0]]))

    print("dictionary: {}".format(dictionary))

    return ''.join(result_entries)

