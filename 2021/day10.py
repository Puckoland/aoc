lines = open('input.txt').read().splitlines()

parentheses_pair = {')': '(', ']': '[', '}': '{', '>': '<'}
parentheses_points = {')': 3, ']': 57, '}': 1197, '>': 25137}
parentheses_points_autocomplete = {'(': 1, '[': 2, '{': 3, '<': 4}


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
    scores = []
    for line in lines:
        corrupted = False
        stack = []
        for c in line:
            if c not in parentheses_pair.keys():
                stack.append(c)
            else:
                if not stack:
                    continue
                if parentheses_pair[c] != stack.pop():
                    corrupted = True
                    break
        if corrupted:
            continue
        points = 0
        while stack:
            c = stack.pop()
            points *= 5
            points += parentheses_points_autocomplete[c]
        scores.append(points)
    scores.sort()
    print(scores[len(scores) // 2])


part1()
part2()
