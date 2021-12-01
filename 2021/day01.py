lines = open('input.txt', 'r').read().splitlines()
numbers = list(map(lambda x: int(x), lines))


def part1():
    increments = 0
    last = numbers[0]
    for number in numbers:
        if number > last:
            increments += 1
        last = number
    print(increments)


def part2():
    increments = 0
    window = [numbers[0], numbers[1], numbers[2]]
    last = sum(window)
    for number in numbers:
        curr = last - window[0]
        window[0] = window[1]
        window[1] = window[2]
        window[2] = number
        curr += number

        if curr > last:
            increments += 1
        last = curr
    print(increments)


part1()
part2()
