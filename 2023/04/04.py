def load_input():
    lines = open('input.txt', 'r').readlines()
    return list(map(lambda x: x.strip(), lines))


def number_of_winning_numbers(line):
    line = line[line.index(':') + 2:]
    winning, mine = line.split(' | ')
    winning = winning.split()
    mine = mine.split()
    winning = [True if c in winning else False for c in mine]
    return sum(winning)


def part_1(lines):
    points_for_cards = []
    for i, line in enumerate(lines):
        winning = number_of_winning_numbers(line)
        if winning:
            points = pow(2, winning - 1)
            points_for_cards.append(points)
    return sum(points_for_cards)


def part_2(lines):
    number_of_cards = [1 for _ in range(len(lines))]
    for i, line in enumerate(lines):
        winning = number_of_winning_numbers(line)
        for _ in range(number_of_cards[i]):
            if winning:
                for next_index in range(winning):
                    number_of_cards[i + 1 + next_index] += 1
    return sum(number_of_cards)


assert part_1(load_input()) == 20107
assert part_2(load_input()) == 8172507
