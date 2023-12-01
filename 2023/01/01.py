lines = open('input.txt', 'r').readlines()

valid = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def part_1():
    suma = 0
    for line in lines:
        first = ""
        last = ""
        for char in line:
            if char.isdigit():
                if not first:
                    first = char
                last = char
        num = first + last
        suma += int(num)
    return suma


def part_2():
    suma = 0
    for line in lines:
        first = ""
        last = ""
        first_index = len(line)
        last_index = 0
        for i, char in enumerate(line):
            if char.isdigit():
                if not first:
                    first = char
                    first_index = i
                last = char
                last_index = i
        for num_str in valid:
            if num_str in line:
                index = line.index(num_str)
                rindex = line.rindex(num_str)
                if index < first_index:
                    first = valid.index(num_str) + 1
                    first_index = index
                if rindex > last_index:
                    last = valid.index(num_str) + 1
                    last_index = rindex
        num = str(first) + str(last)
        suma += int(num)
    return suma


assert part_1() == 54697
assert part_2() == 54885
