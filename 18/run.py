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

ex1 = """[1,2]
[[1,2],3]
[9,[8,7]]
[[1,9],[8,5]]
[[[[1,2],[3,4]],[[5,6],[7,8]]],9]
[[[9,[3,8]],[[0,9],6]],[[[3,7],[4,9]],3]]
[[[[1,3],[5,3]],[[1,3],[8,7]]],[[[4,9],[6,9]],[[8,2],[7,3]]]]
"""

"""
To reduce a snailfish number, you must repeatedly do the first action in this list that applies to the snailfish number:

    If any pair is nested inside four pairs, the leftmost such pair explodes.
    If any regular number is 10 or greater, the leftmost such regular number splits.

"""


def to_str(l):
    return str(l).replace(" ", "")


ex2 = "[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]"


def add2(a, b):
    a, b = str(a), str(b)
    return to_str([eval(a), eval(b)])


print(add2("[1,  2]", "[[3,4],5]"))
assert add2("[1,2]", "[[3,4],5]") == "[[1,2],[[3,4],5]]"


def explode_at(a, idx):
    a = to_str(a)
    print(a)
    breakpoint()
    # idx is the start of the left number
    # '... [1,2]...'
    #       ^
    # scan left, add 1
    cur = idx
    left_scan_start = cur - 1
    left_num = ""
    while a[cur] != ",":
        left_num += a[cur]
        cur += 1
    cur += 1
    right_num = ""
    while a[cur] != "]":
        right_num += a[cur]
        cur += 1
    right_scan_start = cur
    left_num = int(left_num)
    right_num = int(right_num)
    print(left_num, right_num)

    breakpoint()
    return


def reduce(a):
    a = to_str(a)
    while True:
        depth = 0
        for idx, c in enumerate(a):
            if c == "[":
                depth += 1
            elif c == "]":
                depth -= 1
            if depth >= 4 and c in "0123456789":
                print("explodeat", idx)
                explode_at(a, idx)
                break
        else:
            break


reduce(ex2)


def line2tup(line):
    line = to_str(line)
    pass


def parse_input(data):
    lines = data.strip().splitlines()
    print(f"{len(lines)} lines in {input_file}\n")
    line_groups = data.strip().split("\n\n")  # lines split by double newlines
    parsed = []
    for idx, line in enumerate(lines):
        # parsed.append(eval(line))
        parsed.append(line.strip())

    pprint(parsed)
    print(f"{len(parsed)=}")
    return parsed


print(parse_input(ex1))


def part12(data):
    tot = 0
    for idx, d in enumerate(data):
        if d:
            tot += 1
    return tot


if __name__ == "__main__":
    data = parse_input(data)
    print(data)
