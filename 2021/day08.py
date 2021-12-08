lines = open('input.txt').read().splitlines()
entries = list(map(lambda line: list(map(lambda x: x.split(), line.split('|'))), lines))

ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
KNOWN_LENGTHS = [2, 3, 4, 7]


def part1():
    count = 0
    for entry in entries:
        for out in entry[1]:
            if len(out) in KNOWN_LENGTHS:
                count += 1
    print(count)


def get_missing(word):
    chars = ALPHABET[:]
    for c in word:
        chars.remove(c)
    return chars


def get_a_from_seven_and_one(mapa):
    seven = mapa[3][0][:]
    for c in mapa[2][0]:
        seven.remove(c)
    return seven[0]


def get_d_from_zero(mapa):
    for potential in mapa[6]:
        missing = get_missing(potential)[0]
        found = True
        for five_len in mapa[5]:
            if missing not in five_len:
                found = False
                break
        if found:
            return missing


def print_num(alphabet):
    print(
        " {0}{0}{0} \n"
        "{1}   {2}\n"
        "{1}   {2}\n"
        " {3}{3}{3} \n"
        "{4}   {5}\n"
        "{4}   {5}\n"
        " {6}{6}{6} ".format(alphabet['a'], alphabet['b'], alphabet['c'],
                               alphabet['d'], alphabet['e'], alphabet['f'], alphabet['g'])
    )


def decipher_word(word, alphabet):
    if len(word) == 7:
        return 8
    if len(word) == 2:
        return 1
    if len(word) == 3:
        return 7
    if len(word) == 4:
        return 4
    if len(word) == 6:
        if alphabet['d'] not in word:
            return 0
        elif alphabet['c'] not in word:
            return 6
        else:
            return 9
    if alphabet['c'] not in word:
        return 5
    if alphabet['f'] not in word:
        return 2
    return 3


def decipher_output(output, alphabet):
    result = 0
    for out in output:
        result = (result * 10) + decipher_word(out, alphabet)
    return result


def get_alphabet(entry):
    occurrence_stat = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0}
    alphabet = {}

    words_by_length = {2: [], 3: [], 4: [], 5: [], 6: [], 7: []}
    for config in entry:
        for c in config:
            occurrence_stat[c] += 1
        words_by_length[len(config)].append([char for char in config])
    alphabet['a'] = get_a_from_seven_and_one(words_by_length)
    alphabet['d'] = get_d_from_zero(words_by_length)

    for c in occurrence_stat:
        if occurrence_stat[c] == 4:
            alphabet['e'] = c
        elif occurrence_stat[c] == 6:
            alphabet['b'] = c
        elif occurrence_stat[c] == 9:
            alphabet['f'] = c
        elif occurrence_stat[c] == 8 and c != alphabet['a']:
            alphabet['c'] = c
        elif occurrence_stat[c] == 7 and c != alphabet['d']:
            alphabet['g'] = c
    return alphabet


def part2():
    suma = 0
    for entry in entries:
        suma += decipher_output(entry[1], get_alphabet(entry[0]))
    print(suma)


part1()
part2()
