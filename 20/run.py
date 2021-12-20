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

decoder = []


def parse_input():
    lines = data.strip().splitlines()
    print(f"{len(lines)} lines in {input_file}\n")
    global decoder
    decoder = [i == "#" for i in lines[0]]
    print(decoder)
    pic = defaultdict(bool)
    for yidx, line in enumerate(lines[2:]):
        for xidx, char in enumerate(line):
            pic[(xidx, yidx)] = char == "#"
    return pic


def bounding_box(pic):
    minx = miny = float("inf")
    maxx = maxy = float("-inf")
    for (x, y), val in pic.items():
        if val:
            minx = min(x, minx)
            maxx = max(x, maxx)
            miny = min(y, miny)
            maxy = max(y, maxy)
    return minx - 2, miny - 2, maxx + 2, maxy + 2


def round(pic):
    nu_pic = defaultdict(bool)
    min_x, min_y, max_x, max_y = bounding_box(pic)
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            sofar = ""
            for dy, dx in sorted(product((-1, 0, 1), (-1, 0, 1))):
                nx, ny = x + dx, y + dy
                sofar += f"{int(pic[(nx, ny)])}"
            nu_pic[(x, y)] = decoder[int(sofar, 2)]
    return nu_pic


def show2d(pic):
    min_x, min_y, max_x, max_y = bounding_box(pic)
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            print("#" if pic[(x, y)] else ".", end="")
        print()


# too high: 6581
# too high: 6006
def alight(pic):
    return sum(pic.values())


def part12(pic):
    for g in range(0, 3):
        print("-----")
        print(f"{g=}")
        show2d(pic)
        print(alight(pic))
        pic = round(pic)


if __name__ == "__main__":
    pic = parse_input()
    part12(deepcopy(pic))
