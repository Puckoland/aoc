lines = open('input.txt', 'r').read().splitlines()

SIZE = 1000


def count_more_than_1(board):
    x = 0
    for line in board:
        print(line)
        for num in line:
            if num >= 2:
                x += 1
    return x


def part1():
    board = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
    for line in lines:
        x = line.split()
        x1, y1 = x[0].split(',')
        x2, y2 = x[2].split(',')
        x1 = int(x1)
        y1 = int(y1)
        x2 = int(x2)
        y2 = int(y2)
        if x1 != x2 and y1 != y2:
            continue
        if x1 == x2:
            for i in range(min(y1, y2), max(y1, y2) + 1):
                board[i][x1] += 1
        else:
            for i in range(min(x1, x2), max(x1, x2) + 1):
                board[y1][i] += 1
    print(count_more_than_1(board))


def part2():
    board = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
    for line in lines:
        x = line.split()
        x1, y1 = x[0].split(',')
        x2, y2 = x[2].split(',')
        x1 = int(x1)
        y1 = int(y1)
        x2 = int(x2)
        y2 = int(y2)
        if x1 == x2:
            for i in range(min(y1, y2), max(y1, y2) + 1):
                board[i][x1] += 1
        elif y1 == y2:
            for i in range(min(x1, x2), max(x1, x2) + 1):
                board[y1][i] += 1
        else:
            print(x1, y1, x2, y2)
            if x1 < x2:
                for i in range(x1, x2 + 1):
                    if y1 < y2:
                        board[y1 + (i - x1)][i] += 1
                    else:
                        board[y1 - (i - x1)][i] += 1
            else:
                for i in range(x2, x1 + 1):
                    if y1 < y2:
                        board[y2 - (i - x2)][i] += 1
                    else:
                        board[y2 + (i - x2)][i] += 1

    print(count_more_than_1(board))


part1()
part2()
