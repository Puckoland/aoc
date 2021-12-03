lines = open('input.txt', 'r').read().splitlines()
lines = list(map(lambda line: [int(c) for c in line], lines))

num_of_bits = len(lines[0])
num_of_lines = len(lines)


def part1():
    ones = [0] * num_of_bits
    for line in lines:
        for i in range(num_of_bits):
            ones[i] += line[i]
    gamma = 0
    epsilon = 0
    for i in range(num_of_bits):
        most_common_bit = 0 if ones[i] <= num_of_lines // 2 else 1
        gamma = (gamma << 1) | most_common_bit
        epsilon = (epsilon << 1) | (1 - most_common_bit)
    print(gamma * epsilon)


def parse_num(bits):
    number = 0
    for bit in bits:
        number = (number << 1) | bit
    return number


def most_common(data, bit_position, preferred):
    num_of_lines_half = len(data) / 2
    ones = 0
    for entry in data:
        ones += entry[bit_position]
    return 1 if ones > num_of_lines_half else 0 if ones < num_of_lines_half else preferred


def least_common(data, bit_position, preferred):
    return 1 - most_common(data, bit_position, 1 - preferred)


def rating(preferred, f):
    lines_copy = lines.copy()
    while len(lines_copy) > 1:
        for pos in range(num_of_bits):
            bit_to_preserve = f(lines_copy, pos, preferred)
            lines_copy = list(filter(lambda line: line[pos] == bit_to_preserve, lines_copy))
            if len(lines_copy) == 1:
                break
    return parse_num(lines_copy[0])


def part2():
    oxygen_rating = rating(1, most_common)
    co2_rating = rating(0, least_common)
    print(oxygen_rating * co2_rating)


part1()
part2()
