def load_input():
    parts = open('input.txt', 'r').read().split("\n\n")
    parts = list(map(lambda x: x.strip(), parts))
    seeds = parts[0].split(": ")[1].split(" ")
    seeds = list(map(lambda x: int(x), seeds))
    maps_string = parts[1:]
    maps_string = list(map(lambda x: x.split("\n")[1:], maps_string))
    maps = []
    for mapa in maps_string:
        mappings = []
        for line in mapa:
            mapping = list(map(lambda x: int(x), line.split()))
            mappings.append(mapping)
        maps.append(mappings)
    return seeds, maps


def part_1(inp):
    seeds, maps = inp
    for mappings in maps:
        for i, seed in enumerate(seeds):
            flag = True
            for mapping in mappings:
                if seed in range(mapping[1], mapping[1] + mapping[2] + 1) and flag:
                    seeds[i] = mapping[0] + (seed - mapping[1])
                    flag = False
    return min(seeds)


def map_seed_range(mappings, seed_min, seed_max):
    new_seeds = []
    flag = True
    for mapping in mappings:
        intersection = range(max(seed_min, mapping[1]), min(seed_max, mapping[1] + mapping[2] - 1) + 1)
        if intersection and flag:
            flag = False
            diff = mapping[0] - mapping[1]
            new_seeds.append(intersection[0] + diff)
            new_seeds.append(intersection[-1] + 1 - intersection[0])
            if seed_min < intersection[0]:
                new_seeds.append(seed_min)
                new_seeds.append(intersection[0] - seed_min)
            if intersection[-1] < seed_max:
                new_seeds.append(intersection[-1] + 1)
                new_seeds.append(seed_max - intersection[-1])
            break
    if flag:
        new_seeds.append(seed_min)
        new_seeds.append(seed_max - seed_min + 1)
    return new_seeds


def num_of_seeds(seeds):
    return sum([seeds[i] for i in range(1, len(seeds), 2)])


def part_2(inp):
    seeds, maps = inp
    test = num_of_seeds(seeds)
    for mappings in maps:
        done = []
        while seeds:
            seed_min = seeds.pop(0)
            seed_max = seed_min + seeds.pop(0) - 1
            new_seed_ranges = map_seed_range(mappings, seed_min, seed_max)
            done.append(new_seed_ranges[0])
            done.append(new_seed_ranges[1])
            seeds.extend(new_seed_ranges[2:])
        seeds = done
        assert num_of_seeds(seeds) == test
    seeds = [seeds[i] for i in range(0, len(seeds), 2)]
    return min(seeds)


assert part_1(load_input()) == 621354867
assert part_2(load_input()) == 15880236
