import os
import sys
from collections import *
from pprint import pprint
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
        lines = data.strip().splitlines()
except:
    print("no " + input_file)
    data, lines = "", []


def ans(answer):
    # store answer to clipboard
    from shutil import which

    xclip_path = which("xclip")
    if xclip_path is not None:
        os.system(f'echo "{answer}"| {xclip_path} -selection clipboard -in')
        print("\t", answer, "| in clipboard\n")
    else:
        print(f"\t {answer} | (answer)\n")


############### boilerplate ###################################################


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


def parse_input():
    lines = data.strip().splitlines()
    print(f"{len(lines)} lines in {input_file}\n")
    nums = lines[0].split("target area: ")[1]
    xs, ys = nums.split(", ")
    x1, x2 = ints(xs.split("=")[1].split(".."))
    y1, y2 = ints(ys.split("=")[1].split(".."))
    goal_area = set()
    miny = float("inf")
    for x in range(min(x1, x2), max(x1, x2) + 1):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            goal_area.add((x, y))
            miny = min(y, miny)
    return goal_area, miny


def show2d(board, dims):
    max_x, max_y = dims
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            draw_cell = (x, y)
            print(board[draw_cell], end="")
        print("")


def fire(vels, goaly):
    xvel, yvel = vels
    goal, miny = goaly
    x = y = 0
    highest = y
    while True:
        if (x, y) in goal:
            return True, highest
        else:
            x += xvel
            y += yvel
            highest = max(y, highest)
            # drag
            if x == 0:
                pass
            elif xvel > 0:
                xvel -= 1
            elif xvel < 0:
                xvel += 1
            # gravity
            yvel -= 1
        if y < miny:
            return False, float("-inf")


if __name__ == "__main__":
    goaly = parse_input()
    best = float("-inf")
    seen = set()
    for x in range(0, 200):
        for y in range(-150, 1000):
            hit, height = fire((x, y), goaly)
            if hit:
                seen.add((x, y))
                print((x, y))
                if height > best:
                    best = height
                    print(x, y, best)
    print("part 1")
    ans(best)
    print("part 2")
    ans(len(seen))
