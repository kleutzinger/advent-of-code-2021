import os
import sys
from collections import *
from copy import deepcopy
from itertools import *

# change to dir of script
os.chdir(os.path.dirname(os.path.abspath(__file__)))
input_file = "input.txt"
if "s" in sys.argv:
    input_file = "input_small.txt"
try:
    with open(input_file) as f:
        data = f.read()  # entire file as string
        lines = data.splitlines()
except:
    print("no " + input_file)
    data, lines = "", []


def ans(answer):
    # store answer to clipboard
    from distutils.spawn import find_executable

    xclip_path = find_executable("xclip")
    if xclip_path:
        os.system(f'echo "{answer}"| {xclip_path} -selection clipboard -in')
        print("\t", answer, "| in clipboard\n")
    else:
        print(f"\t {answer} | (answer)\n")


def coords(arr2d):
    # return [(x0,y0), (x1, y0), ...]
    for y in range(len(arr2d)):
        for x in range(len(arr2d[y])):
            yield (x, y)


############### end of boilerplate ############################################


### PART 1 ###


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
        print(f"\n X = {board[coord[1]][coord[0]]}")


def part12(data):
    # build board
    board = []
    for line in data.strip().split("\n"):
        row = []
        for c in line.strip():
            row.append(int(c))
        board.append(row)

    def neighbors(coord):
        x, y = coord
        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if (0 <= nx < len(board[0])) and (0 <= ny < len(board)):
                yield (nx, ny)

    risk = 0
    basins = []
    for x, y in coords(board):
        for nx, ny in neighbors((x, y)):
            cur = board[y][x]
            friend = board[ny][nx]
            if cur >= friend:
                break
        else:
            basins.append((x, y))
            risk += 1 + cur
    ans(risk)  # 480

    ### PART 2 ###

    print(f"basins: {len(basins)}")

    def dfs(coord):
        nonlocal seen
        # show2d(board, coord, seen)
        x, y = coord
        nbs = []
        for nx, ny in neighbors(coord):
            nval = board[ny][nx]
            val = board[y][x]
            if ((nx, ny) not in seen) and (nval > val) and (nval < 9):
                nbs.append((nx, ny))
                seen.add((nx, ny))
        seen.add(coord)
        global_seen.add(coord)
        return 1 + sum([dfs(i) for i in nbs])

    global_seen = set()  # for printing big board
    sizes = []
    for low_point in basins:
        seen = set()
        basin_size = dfs(low_point)
        sizes.append(basin_size)

    if "v" in sys.argv:
        show2d(board, None, global_seen)

    out = 1
    # could use reduce here
    for s in sorted(sizes, reverse=True)[:3]:
        out *= s
    ans(out)  # 1045660
    return


if __name__ == "__main__":
    part12(data)
