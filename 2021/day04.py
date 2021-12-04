BOARD_SIZE = 5
MARK = -1

lines = open('input.txt', 'r').read().splitlines()
NUM_OF_BOARDS = (len(lines) - 1) // 6


def parse_ints(strings):
    return list(map(lambda num: int(num), strings))


def parse_board(start_row, end_row):
    return [parse_ints(lines[i].split()) for i in range(start_row, end_row)]


def parse_boards():
    return [parse_board(2 + i * (BOARD_SIZE + 1), 1 + (i + 1) * (BOARD_SIZE + 1)) for i in range(NUM_OF_BOARDS)]


def remove_drawn(board, draw):
    for (y, line) in enumerate(board):
        for (x, num) in enumerate(line):
            if num == draw:
                board[y][x] = MARK
                return


def evaluate(boards):
    for board in boards:
        winning_column = [True] * BOARD_SIZE
        for (y, line) in enumerate(board):
            winning_line = True
            for (x, num) in enumerate(line):
                if num != MARK:
                    winning_column[y] = False
                    winning_line = False
                    break
            if winning_line:
                return board
        if True in winning_column:
            return board
    return None


def get_result(board, draw):
    suma = 0
    for line in board:
        for num in line:
            if num != MARK:
                suma += num
    print(suma * draw)


def part1():
    draws = parse_ints(lines[0].split(','))
    boards = parse_boards()
    for draw in draws:
        for board in boards:
            remove_drawn(board, draw)
        winning = evaluate(boards)
        if winning is not None:
            return get_result(winning, draw)


part1()
