import os
import sys
from collections import *
from copy import deepcopy
from itertools import *
from pprint import pprint

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
    def to_sets(d):
        return [set(i) for i in d]

    "cefbd dcg dcfgbae bdeafg gfcaed ecbgd bcag bdacge cg bedag | cebdg egcfda gdacbe badefg"
    l, r = line.split(" | ")
    l, r = to_sets(l.split(" ")), to_sets(r.split(" "))
    return l, r


lines = [line_transform(line) for line in lines]


o = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"


def part1(data):
    tot = 0
    for d in data:
        for s in d:
            if len(s) in [2, 3, 4, 7]:
                tot += 1
    return tot
    for d in data:
        if len(d) == 2:
            one = d
            tot += 1
        if len(d) == 3:
            seven = d
            tot += 1
        if len(d) == 4:
            four = d
            tot += 1
        if len(d) == 7:
            eight = d
            tot += 1
        print(d)
    return tot

    tot = 0
    for idx, d in enumerate(data):
        if d:
            tot += 1
    return tot


"""
  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg

"""


def line_to_output(l, r):
    """
    2: one
    3: seven
    4: four
    5: two, three, five
    6: zero, six, nine
    7: eight

    """
    sig = dict()

    def go(num, d_):
        nonlocal sig
        if num in sig.keys():
            pprint(sig)
            print(f"{num=} already in sig")
            exit(1)
        sig[num] = d_

    for d in l:
        if len(d) == 2:
            go(1, d)
        if len(d) == 3:
            go(7, d)
        if len(d) == 4:
            go(4, d)
        if len(d) == 7:
            go(8, d)
    for d in l:
        if len(d) == 6 and len(d - sig[1]) == 5:
            go(6, d)
    for d in l:
        if len(d) == 6 and sig[4].issubset(d):
            go(9, d)
    for d in l:
        if len(d) == 6 and d not in sig.values():
            go(0, d)
    for d in l:
        if len(d) == 5 and d.issubset(sig[6]):
            go(5, d)
    for d in l:
        if len(d) == 5 and sig[1].issubset(d) and d.issubset(sig[9]):
            go(3, d)
    for d in l:
        if d not in sig.values():
            go(2, d)

    out = ""
    for d in r:
        for num, v in sig.items():
            if d == v:
                out += str(num)

    return int(out)


### PART 2 ###


def part2(lines):
    pass


if __name__ == "__main__":
    data = [l[1] for l in lines]
    ans(part1(deepcopy(data)))  # 274
    tot = 0
    for line in lines:
        tot += line_to_output(*line)
    ans(tot)  # 1012089
