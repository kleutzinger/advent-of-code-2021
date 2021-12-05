import os
import shutil
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


### PART 1 ###

ints = lambda l: list(map(int, l))


def line_transform(line):
    "I run on each line of the input"
    # split = [line.split() for line in lines]

    # return int(line)
    # 0,9 -> 5,9
    l, r = line.split(" -> ")
    l = ints(l.split(","))
    r = ints(r.split(","))
    return l, r


def filt(pair):
    (x1, y1), (x2, y2) = pair
    if x1 == x2 or y1 == y2:
        return True
    return False


def build_board(pairs):
    board = defaultdict(int)
    for pair in pairs:
        (x1, y1), (x2, y2) = pair
        if x1 == x2:
            # vert
            for y in range(min(y1, y2), max(y1, y2) + 1):
                board[(x1, y)] += 1
        elif y1 == y2:
            # horiz
            for x in range(min(x1, x2), max(x1, x2) + 1):
                board[(x, y1)] += 1
        else:
            cur_x, cur_y = x1, y1
            dest_x, dest_y = x2, y2
            if cur_x < dest_x:
                dx = 1
            else:
                dx = -1
            if cur_y < dest_y:
                dy = 1
            else:
                dy = -1
            while cur_x != dest_x:
                board[(cur_x, cur_y)] += 1
                cur_x += dx
                cur_y += dy
            board[(cur_x, cur_y)] += 1
    return board


def count_more(board, n):

    tot = 0
    for val in board.values():
        if val >= n:
            tot += 1
    return tot


lines = [line_transform(line) for line in lines]


def part1(lines):
    b = build_board(filter(filt, lines))
    return count_more(b, 2)


### PART 2 ###


def part2(lines):
    b = build_board(lines)
    return count_more(b, 2)


if __name__ == "__main__":
    p1_ans = part1(deepcopy(lines))
    ans(p1_ans) # 4826
    p2_ans = part2(deepcopy(lines))
    # not 16772
    ans(p2_ans) # 16793
