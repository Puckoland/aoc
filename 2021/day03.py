lines = open('input.txt', 'r').read().splitlines()


def part1():
    num_of_bits = len(lines[0])
    num_of_lines = 0
    ones = [0] * num_of_bits
    for line in lines:
        num_of_lines += 1
        for i in range(num_of_bits):
            ones[i] += int(line[i])
    gamma = 0
    epsilon = 0
    for i in range(num_of_bits):
        most_common_bit = 0 if ones[i] <= num_of_lines // 2 else 1
        gamma = (gamma << 1) | most_common_bit
        epsilon = (epsilon << 1) | (1 - most_common_bit)
    print(gamma * epsilon)


part1()
