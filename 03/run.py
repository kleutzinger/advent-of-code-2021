import os
import sys
import shutil
from itertools import *
from collections import *
from copy import deepcopy

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
    zeroes= defaultdict(int)
    ones = defaultdict(int)
    for idx, line in enumerate(lines):
        for bidx, val in enumerate(line):
            if val == '0':
                zeroes[bidx] += 1
            else:
                ones[bidx] += 1
    print(zeroes, ones)
    gamma = ''
    epsilon = ''
    for i in range(len(line)):
        if zeroes[i] > ones[i]:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'
    #not 4095
    a = (int(gamma, 2) * int(epsilon, 2))
    return a




    return tot


### PART 2 ###

def count_idx_n(lines, n):
    zeroes= defaultdict(int)
    ones = defaultdict(int)
    for idx, line in enumerate(lines):
        for bidx, val in enumerate(line):
            if val == '0':
                zeroes[bidx] += 1
            else:
                ones[bidx] += 1
    return zeroes[n], ones[n]

def part2(lines):
    o = oxy(deepcopy(lines))
    c = co2(deepcopy(lines))
    return int(o, 2) * int(c, 2)

    pass

def oxy(lines):
    cur_idx = 0
    while len(lines) > 1:
        z, o = count_idx_n(lines, cur_idx)
        look = str(int(o >= z))
        lines = [i for i in lines if i[cur_idx] == look]
        cur_idx += 1
    return lines[0]

def co2(lines):
    cur_idx = 0
    while len(lines) > 1:
        z, o = count_idx_n(lines, cur_idx)
        look = str(int(o < z))
        lines = [i for i in lines if i[cur_idx] == look]
        cur_idx += 1
    return lines[0]


if __name__ == "__main__":
    p1_ans = part1(deepcopy(lines))
    ans(p1_ans) # 4160394
    p2_ans = part2(deepcopy(lines))
    ans(p2_ans) # 4125600
