lines = open('input.txt').read().splitlines()

parentheses_pair = {')': '(', ']': '[', '}': '{', '>': '<'}
parentheses_points = {')': 3, ']': 57, '}': 1197, '>': 25137}


def part1():
    corrupted = []
    for line in lines:
        stack = []
        for c in line:
            if c not in parentheses_pair.keys():
                stack.append(c)
            else:
                if not stack:
                    continue
                if parentheses_pair[c] != stack.pop():
                    corrupted.append(c)
    print(sum(list(map(lambda x: parentheses_points[x], corrupted))))


def part2():
    pass


part1()
part2()
