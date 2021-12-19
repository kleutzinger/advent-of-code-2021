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
    line_groups = data.strip().split("\n\n")  # lines split by double newlines

    scanners = []
    for idx, scanner in enumerate(line_groups):
        cur_scanner = []
        for line in scanner.splitlines()[1:]:
            coords = tuple(comma_ints(line))
            cur_scanner.append(coords)
        scanners.append(cur_scanner)

    pprint(scanners)
    print(f"{len(scanners)=}")
    return scanners


def part12(data):
    tot = 0
    for idx, d in enumerate(data):
        if d:
            tot += 1
    return tot


if __name__ == "__main__":
    data = parse_input()
    part12(deepcopy(data))
