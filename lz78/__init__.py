
def encode(input_data):
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


def decode(input_data):
    pairs = pairwise(input_data)
    result = ""

    for pointer, newchar in pairs:
        if(pointer == 0):
            result += newchar
        else:
            result += "{}{}".format(get_representation(pointer, pairs), newchar if newchar is not None else "")

    return result


def get_representation(pointer, pairs):
    new_pair = pairs[pointer - 1]
    if new_pair[0] == 0:
        return new_pair[1]
    else:
        return get_representation(new_pair[0], pairs) + new_pair[1]


def pairwise(iterable):
    "s -> (s0, s1), (s2, s3), (s4, s5), ..."
    a = iter(iterable)
    return list(zip(a, a))
