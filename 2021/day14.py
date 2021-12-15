lines = open('input.txt').read().splitlines()
template = lines[0]
rules = dict(map(lambda x: x.split(" -> "), lines[2:]))


def change_rules():
    for key in rules:
        rules[key] = key[0] + rules[key], rules[key] + key[1]


def get_result(pair_counts):
    # Add first letter
    letters = {template[0]: 1}
    for key in pair_counts:
        second = key[1]
        if second in letters:
            letters[second] += pair_counts[key]
        else:
            letters[second] = pair_counts[key]
    return letters[max(letters, key=letters.get)] - letters[min(letters, key=letters.get)]


def do(steps):
    pair_counts = {}
    for i in range(len(template) - 1):
        pair = template[i] + template[i + 1]
        if pair in pair_counts:
            pair_counts[pair] += 1
        else:
            pair_counts[pair] = 1
    for _ in range(steps):
        new_counts = {}
        for pair in pair_counts:
            count = pair_counts[pair]
            first = rules[pair][0]
            second = rules[pair][1]
            if first in new_counts:
                new_counts[first] += count
            else:
                new_counts[first] = count
            if second in new_counts:
                new_counts[second] += count
            else:
                new_counts[second] = count
        pair_counts = new_counts
    print(get_result(pair_counts))


def part1():
    do(10)


def part2():
    do(40)


change_rules()
part1()
part2()
