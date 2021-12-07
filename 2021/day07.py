lines = open('input.txt', 'r').read().split(',')
nums = list(map(lambda x: int(x), lines))


def part1():
    median = sorted(nums)[len(nums) // 2]
    suma = 0
    for num in nums:
        suma += abs(num - median)
    print(suma)


def part2():
    sums = []
    for i in range(max(nums)):
        suma = 0
        for num in nums:
            diff = abs(num - i)
            suma += (diff + 1) * diff // 2
        sums.append(suma)
    print(min(sums))


part1()
part2()
