lines = open('input.txt').read().splitlines()
start = lines[0]
rules = dict(map(lambda x: x.split(" -> "), lines[2:]))


def change_rules():
    for key in rules:
        rules[key] = key[0] + rules[key], rules[key] + key[1]


def reduce_rules():
    for key in rules:
        fi = key[0] + rules[key]
        se = rules[key] + key[1]
        rules[key] = key[0] + rules[fi] + rules[key] + rules[se]


def get_result(template):
    # First letter
    counts = {start[0]: 1}
    for key in template:
        se = key[1]
        if se in counts:
            counts[se] += template[key]
        else:
            counts[se] = template[key]
    return counts[max(counts, key=counts.get)] - counts[min(counts, key=counts.get)]


def do(steps):
    template = {}
    for i in range(len(start) - 1):
        pair = start[i] + start[i + 1]
        if pair in template:
            template[pair] += 1
        else:
            template[pair] = 1
    for _ in range(steps):
        new_tem = {}
        for pair in template:
            count = template[pair]
            fi = rules[pair][0]
            se = rules[pair][1]
            if fi in new_tem:
                new_tem[fi] += count
            else:
                new_tem[fi] = count
            if se in new_tem:
                new_tem[se] += count
            else:
                new_tem[se] = count
        template = new_tem
    print(get_result(template))


def part1():
    do(10)


def part2():
    do(40)


change_rules()
part1()
part2()
