def encode(input_data, dictionary=["a", "b", "c"]):
    result = []

    current_word = ""
    main_index = 0
    while main_index < len(input_data):
        sub_index = main_index
        while (current_word == "" or current_word in dictionary) and not sub_index == len(input_data):
            current_word = input_data[main_index:sub_index + 1]
            sub_index += 1

        if sub_index == len(input_data):
            word_to_append = current_word
        else:
            # This is the last word. Simply append it to the encoded result
            word_to_append = current_word[:-1]  # Append the previous word to the encoded list
            dictionary.append(current_word)  # Append current word to dictionary

        index_in_dictionary = dictionary.index(word_to_append) + 1
        result.append(index_in_dictionary)

        main_index += len(word_to_append)

    return result


def decode(input_data):
    pass
