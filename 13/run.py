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


############### boilerplate ###################################################

line_groups = data.split("\n\n")  # lines split by double newlines
# line_groups = [l.strip() for l in line_groups]  # remove trailing newlines
# print(lines)
print(f"{len(lines)} lines in {input_file}\n")


def coords(arr2d):
    # return [(x0,y0), (x1, y0), ...]
    for y in range(len(arr2d)):
        for x in range(len(arr2d[y])):
            yield (x, y)


def rotate2d(l):
    "rotate a 2d list counter_clockwise once"
    nu = deepcopy(l)
    return list(zip(*nu))[::-1]


def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


strips = lambda l: list(map(str.strip, l))
ints = lambda l: list(map(int, l))
commas = lambda s: s.split(",")
comma_ints = lambda s: ints(strips(s.split(",")))

L, I, D, S = list, int, dict, set
P, E, R, M = print, enumerate, range, map

############### end of boilerplate ############################################


### PART 1 ###


def line_transform(line):
    "I run on each line of the input"
    # split = [line.split() for line in lines]
    # return int(line)
    return line


lines = [line_transform(line) for line in lines]

if len(lines):
    l = lines[0]

try:
    nums = [int(i.strip()) for i in lines[0]]
except:
    pass


def max_dims(board):
    maxx, maxy = float("-inf"), float("-inf")
    for x, y in board.keys():
        maxx, maxy = max(maxx, x), max(maxy, y)
    return maxx, maxy


def do_fold(board, fold):
    axis, pivot = fold
    max_x, max_y = max_dims(board)
    if axis == "y":
        """
        0110
        0000
        ----
        0000
        0111
        """
        nu_board = defaultdict(bool)
        for dy in range(0, pivot + 1):
            below_y, above_y = pivot - dy, pivot + dy
            for c in range(max_x + 1):
                if board[(c, below_y)] or board[(c, above_y)]:
                    nu_board[(c, above_y)] = True
        print(len(nu_board.items()))
        return nu_board
    elif axis == "x":
        """
        01|10
        00|00
        00|00
        01|11
        """
        nu_board = defaultdict(bool)
        for dx in range(0, pivot + 1):
            left_x, right_x = pivot - dx, pivot + dx
            for c in range(max_y + 1):
                if board[(left_x, c)] or board[(right_x, c)]:
                    nu_board[(left_x, c)] = True
        print(len(nu_board.items()))
        return nu_board


from pprint import pprint


def part1(data):
    coord_lines, fold_lines = line_groups
    dots = []
    for coord_line in coord_lines.split("\n"):
        a, b = coord_line.split(",")
        dots.append((int(a), int(b)))

    folds = []
    for fold in fold_lines.split("\n")[:-1]:
        axis = fold.split("=")[0][-1]
        mag = int(fold.split("=")[1])
        folds.append((axis, mag))

    board = defaultdict(bool)
    for coord in dots:
        board[coord] = True

    for fold in folds:
        board = do_fold(board, fold)  # 720


if __name__ == "__main__":
    ans(part1(deepcopy(data)))
    # p2_ans = part2(deepcopy(lines))
    # ans(p2_ans)
