with open("input.txt", "r") as f:
    lines = f.readlines()


def coords(arr2d):
    # return [(x0,y0), (x1, y0), ...]
    for y in range(len(arr2d)):
        for x in range(len(arr2d[y])):
            yield (x, y)


def neighbors(coord):
    x, y = coord
    for dx, dy in [
        (0, 1),
        (1, 0),
        (-1, 0),
        (0, -1),
        (1, 1),
        (-1, 1),
        (1, -1),
        (-1, -1),
    ]:
        nx, ny = x + dx, y + dy
        if (0 <= nx < len(board[0])) and (0 <= ny < len(board)):
            yield (nx, ny)


flashes_total = 0


def show2d(board, coord, seen):
    for y in range(len(board)):
        for x in range(len(board[0])):
            draw_cell = (x, y)
            if draw_cell == coord:
                print("X", end="")
            elif draw_cell in seen:
                print("·", end="")
            else:
                print(board[y][x], end="")
        print()
    if coord:
        print(f"\n {coord=}")


def ten_pres(board):
    for x, y in coords(board):
        if board[y][x] > 9:
            return True
    return False


def step(board):
    size = len(board * len(board[0]))
    for x, y in coords(board):
        board[y][x] += 1
    flashed = set()
    done = False

    rounds = 0
    while True:
        to_flash = set()
        for x, y in coords(board):
            cur = board[y][x]
            if cur > 9 and (x, y) not in flashed:
                to_flash.add((x, y))
        if len(to_flash) == 0:
            break
        for fx, fy in to_flash:
            for nx, ny in neighbors((fx, fy)):
                board[ny][nx] += 1
            flashed.add((fx, fy))
            if size == len(flashed):
                print("all flashed! pt 2 ans:")
                return None
        to_flash = set()

    for fx, fy in flashed:
        board[fy][fx] = 0

    global flashes_total
    flashes_total += len(flashed)
    #show2d(board, None, flashed)

    return board


board = []
for line in lines:
    line = line.strip()
    row = []
    for c in line:
        row.append(int(c))
    board.append(row)


from copy import deepcopy

show2d(board, None, set())
for gen in range(999999):
    if gen == 100:
        print("part 1", flashes_total)
    board = step(deepcopy(board))
    if board is None:
        print("part 2", gen+1)
        exit()


