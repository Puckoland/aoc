lines = open('input.txt', 'r').read().splitlines()
lines = list(map(lambda x: int(x), lines))


def part1():
    increments = 0
    last = lines[0]
    for line in lines:
        if line > last:
            increments += 1
        last = line
    print(increments)


def part2():
    increments = 0
    window = [lines[0], lines[1], lines[2]]
    last = sum(window)
    for line in lines:
        curr = last - window[0]
        window[0] = window[1]
        window[1] = window[2]
        window[2] = line
        curr += line

        if curr > last:
            increments += 1
        last = curr
    print(increments)


part1()
part2()
