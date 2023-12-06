def load_input():
    parts = open('input.txt', 'r').readlines()
    parts = list(map(lambda x: x.strip(), parts))
    return list(map(lambda x: x.split(":")[1].strip(), parts))


def parse_input_part_1(parts):
    parts = list(map(lambda x: x.split(), parts))
    parts = list(map(lambda x: list(map(lambda y: int(y), x)), parts))
    return [(parts[0][i], parts[1][i]) for i in range(len(parts[0]))]


def parse_input_part_2(parts):
    parts = list(map(lambda x: x.replace(" ", ""), parts))
    parts = list(map(lambda x: int(x), parts))
    return parts[0], parts[1]


def test_win(race, start_time):
    time, dist = race
    speed = start_time
    time_rest = time - start_time
    dist_travelled = speed * time_rest
    return dist_travelled > dist


def bin_search_first_win(race, left, right):
    mid = (left + right) // 2
    if test_win(race, mid) and not test_win(race, mid - 1):
        return mid
    if test_win(race, mid - 1):
        return bin_search_first_win(race, left, mid - 1)
    return bin_search_first_win(race, mid + 1, right)


def bin_search_last_win(race, left, right):
    mid = (left + right) // 2
    if test_win(race, mid) and not test_win(race, mid + 1):
        return mid
    if test_win(race, mid + 1):
        return bin_search_last_win(race, mid + 1, right)
    return bin_search_last_win(race, left, mid - 1)


def number_of_options_to_win_race(race):
    time, dist = race

    first_win = bin_search_first_win(race, 1, time - 1)
    last_win = bin_search_last_win(race, 1, time - 1)

    return last_win - first_win + 1


def part_1(parts):
    races = parse_input_part_1(parts)
    res = 1
    for race in races:
        res *= number_of_options_to_win_race(race)
    return res


def part_2(parts):
    race = parse_input_part_2(parts)
    return number_of_options_to_win_race(race)


assert part_1(load_input()) == 1312850
assert part_2(load_input()) == 36749103
