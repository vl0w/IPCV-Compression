import copy


def encode(input_data, base_dictionary=["a", "b", "c"]):
    encodings = []
    dictionary = copy.copy(base_dictionary)

    current_word = ""
    main_index = 0
    while main_index < len(input_data):
        sub_index = main_index
        while (current_word == "" or current_word in dictionary) and not sub_index == len(input_data):
            current_word = input_data[main_index:sub_index + 1]
            sub_index += 1

        if current_word not in dictionary:
            dictionary.append(current_word)

        if sub_index == len(input_data):  # End of string
            word_to_append = current_word
        else:  # Append previous word to encoded string
            word_to_append = current_word[:-1]

        try:
            index_in_dictionary = dictionary.index(word_to_append) + 1
        except ValueError:
            raise ValueError("Your base dictionary may be missing the character '{0}'".format(current_word))

        encodings.append(index_in_dictionary)

        main_index += len(word_to_append)

    return encodings


def decode(input_data, base_dictionary=["a", "b", "c"]):
    dictionary = copy.copy(base_dictionary)
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

    return ''.join(result_entries)
