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


def part1(data):
    tot = 0
    board = []
    for line in data.strip().split('\n'):
        row = []
        for c in line.strip():
            row.append(int(c))
            print(c)
        board.append(row)
    def neighbors(coord):
        x, y = coord
        for dx, dy in [(0,1), (1,0), (-1,0), (0,-1)]:
            yield (x+dx, y+dy)
    risk = 0
    for x, y in coords(board):
        for nx, ny in neighbors((x,y)):
            pass
            cur = board[y][x]
            try:
                friend = board[ny][nx]
            except:
                continue
            if cur >= friend:
                break
        else:
            risk += 1 + cur
        pass
    return risk

### PART 2 ###


def part2(lines):
    pass


if __name__ == "__main__":
    ans(part1(deepcopy(data)))
    # p2_ans = part2(deepcopy(lines))
    # ans(p2_ans)
