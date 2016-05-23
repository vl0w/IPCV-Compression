
def compress(input_data):
    # [(pointer, newchar, representation)]
    dictionary = []

    prev_found = 0
    prev_string = ""
    for char in input_data:
        s = prev_string + char
        found = find(s, dictionary)
        if found == 0:
            triple = (prev_found, char, s)
            dictionary.append(triple)
            prev_found = 0
            prev_string = ""
        else:
            prev_string = s
            prev_found = found

    if prev_string != "":
        triple = (prev_found, None, prev_string)
        dictionary.append(triple)


    result = []
    for triple in dictionary:
        result.append(triple[0])
        result.append(triple[1])

    return result


def find(s, dict) -> int:
    for triple in dict:
        if triple[2] == s:
            return dict.index(triple) + 1
    return 0
