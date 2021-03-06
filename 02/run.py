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


def part1(lines):
    tot = 0
    x = 0
    y = 0
    for idx, line in enumerate(lines):
        deg, mag = line.split(" ")
        mag = int(mag)
        if "for" in deg:
            x += mag
        if "down" in deg:
            y += mag
        if "up" in deg:
            y -= mag

    return x * y


### PART 2 ###


def part2(lines):
    x = 0
    y = 0
    aim = 0
    for idx, line in enumerate(lines):
        deg, mag = line.split(" ")
        mag = int(mag)
        if "for" in deg:
            x += mag
            y += aim * mag
        if "down" in deg:
            aim += mag
            # y += mag
        if "up" in deg:
            aim -= mag
            # y -= mag

    return x * y


if __name__ == "__main__":
    p1_ans = part1(deepcopy(lines))
    ans(p1_ans) # 1727835
    p2_ans = part2(deepcopy(lines))
    # not 1659021420056
    # not 1545728430
    ans(p2_ans) # 1544000595
