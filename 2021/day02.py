FORWARD = "forward"
DOWN = "down"
UP = "up"

lines = open('input.txt', 'r').read().splitlines()


def part1():
    x = 0
    depth = 0
    for line in lines:
        command, num = line.split(' ')
        num = int(num)
        if command == FORWARD:
            x += num
        elif command == UP:
            depth -= num
        elif command == DOWN:
            depth += num
    print(x * depth)


def part2():
    x = 0
    depth = 0
    aim = 0
    for line in lines:
        command, num = line.split(' ')
        num = int(num)
        if command == FORWARD:
            x += num
            depth += aim * num
        elif command == UP:
            aim -= num
        elif command == DOWN:
            aim += num
    print(x * depth)


part1()
part2()
