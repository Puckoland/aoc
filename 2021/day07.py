lines = open('input.txt', 'r').read().split(',')
nums = list(map(lambda x: int(x), lines))


def part1():
    median = sorted(nums)[len(nums) // 2]
    suma = 0
    for num in nums:
        suma += abs(num - median)
    print(suma)


part1()
