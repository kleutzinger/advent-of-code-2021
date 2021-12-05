"""
this one went pretty smoothly. for some reason, i called "line segments" pairs.
but everything worked out.

I went back and super-simplified my build_board function. Turns out it's better
if you don't think about special cases.
"""
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


### PART 1 ###

ints = lambda l: tuple(map(int, l))


def line_transform(line):
    """
    input:  "0,9 -> 5,9"
    output: ((0,9), (5,9))
    """
    l, r = line.split(" -> ")
    l = ints(l.split(","))
    r = ints(r.split(","))
    return l, r


def horiz_or_vert(pair):
    "identify horizontal and vertial line segments"
    (x1, y1), (x2, y2) = pair
    if x1 == x2 or y1 == y2:
        return True
    return False


def get_dir(a, b):
    "get the delta in (1,-1,0) to move a towards b"
    if a == b:
        return 0
    if a < b:
        return 1
    if a > b:
        return -1


def build_board(pairs):
    """
    We have a list of line segments defined by coord pairs.
    for each line segment:
        increment the board at each point in the line segment
    [
        ((1,0), (1,3)),
        ((0,0), (0,1))
    ]

    0000    0100    1200
    0000 -> 0100 -> 0100
    0000    0100    0100
    0000    0000    0000
    """
    board = defaultdict(int)
    for pair in pairs:
        (cur_x, cur_y), (dest_x, dest_y) = pair
        dx = get_dir(cur_x, dest_x)
        dy = get_dir(cur_y, dest_y)
        while cur_x != dest_x or cur_y != dest_y:
            board[(cur_x, cur_y)] += 1
            cur_x += dx
            cur_y += dy
        board[(cur_x, cur_y)] += 1
    return board


def count_more(board, n):
    "count how many cells have a value >= n"
    tot = 0
    for val in board.values():
        if val >= n:
            tot += 1
    return tot


lines = [line_transform(line) for line in lines]


def part1(lines):
    b = build_board(filter(horiz_or_vert, lines))
    return count_more(b, 2)


### PART 2 ###


def part2(lines):
    b = build_board(lines)
    return count_more(b, 2)


## EXTRA ##


def show_board(board):
    "print out the board"
    max_x = float("-inf")
    max_y = float("-inf")
    for x, y in board.keys():
        max_x = max(x, max_x)
        max_y = max(y, max_y)
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            val = board[(x, y)]
            if val == 0:
                print(".", end="")
            else:
                print(val, end="")
        print()


if __name__ == "__main__":
    p1_ans = part1(deepcopy(lines))
    ans(p1_ans)  # 4826
    p2_ans = part2(deepcopy(lines))
    # not 16772
    ans(p2_ans)  # 16793
