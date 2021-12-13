coors, folds = open('input.txt').read().split("\n\n")
coors = coors.splitlines()
coors = map(lambda x: x.split(','), coors)
coors = list(map(lambda x: (int(x[1]), int(x[0])), coors))
folds = folds.splitlines()

SIZE = 1500


def fold_by_y(page, y):
    if y <= SIZE // 2:
        for i in range(1, y + 1):
            for x in range(len(page[y])):
                page[y - i][x] = max(page[y - i][x], page[y + i][x])
        return page[:y]

    for i in range(1, SIZE - y + 1):
        for x in range(len(page[y])):
            page[y - i][x] = max(page[y - i][x], page[y + i][x])
    return page[y + 1:]


def fold_by_x(page, x):
    if x <= SIZE // 2:
        for i in range(1, x + 1):
            for y in range(len(page)):
                page[y][x - i] = max(page[y][x - i], page[y][x + i])
        page = [[page[y][x] for x in range(0, x)] for y in range(len(page))]
        return page

    for i in range(1, SIZE - x + 1):
        for y in range(len(page)):
            page[y][x - i] = max(page[y][x - i], page[y][x + i])
    page = [[page[y][x] for x in range(x + 1, SIZE)] for y in range(len(page))]
    return page


def part1():
    page = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
    for y, x in coors:
        page[y][x] = 1
    for fold in folds:
        if 'y' in fold:
            page = fold_by_y(page, int(fold.split('=')[1]))
        else:
            page = fold_by_x(page, int(fold.split('=')[1]))
    print(sum([sum(line) for line in page]))
    for line in page:
        text = ""
        for x in range(len(line)):
            text += ' #'[line[x]]
        print(text)


part1()
