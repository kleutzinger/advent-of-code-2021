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
    def to_sets(d):
        return [set(i) for i in d]
    'cefbd dcg dcfgbae bdeafg gfcaed ecbgd bcag bdacge cg bedag | cebdg egcfda gdacbe badefg'
    l, r = line.split(' | ')
    l, r = to_sets(l.split(' ')), to_sets(r.split(' '))
    return l, r


lines = [line_transform(line) for line in lines]


o = 'acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf'

def part1(data):
    tot = 0
    for d in data:
        for s in d:
            if len(s) in [2,3,4,7]:
                tot += 1
    return tot
    for d in data:
        if len(d) == 2:
            one = d
            tot +=1
        if len(d) == 3:
            seven = d
            tot +=1
        if len(d) == 4:
            four = d
            tot +=1
        if len(d) == 7:
            eight = d
            tot +=1
        print(d)
    return tot
    
    tot = 0
    for idx, d in enumerate(data):
        if d:
            tot += 1
    return tot


### PART 2 ###


def part2(lines):
    pass


if __name__ == "__main__":
    data = [l[1] for l in lines]
    # not 200
    for d in data:
        print(len(d))
    ans(part1(deepcopy(data)))
    # p2_ans = part2(deepcopy(lines))
    # ans(p2_ans)
