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
    return comma_ints(line)


lines = [line_transform(line) for line in lines]


def gen(nums):
    nu_nums = []
    for num in nums:
        if num == 0:
            nu_nums.append(6)
            nu_nums.append(8)
        else:
            nu_nums.append(num - 1)
    return nu_nums


def part1(nums):
    tot = 0
    nums = lines[0].copy()
    for d in range(80):
        nums = gen(nums)
    return len(nums)


### PART 2 ###


def gen2(nums, gens=256):
    fish = Counter(nums)
    for gen in range(gens):
        # print(gen, [(x, fish[x]) for x in range(9)])
        nu_fish = Counter()
        for idx in range(9):
            fish_count = fish[idx]
            if idx == 0:
                nu_fish[8] += fish[0]
                nu_fish[6] += fish[0]
            else:
                nu_fish[idx - 1] += fish_count
        fish = nu_fish
    return sum(fish.values())


def part2(lines):
    return gen2(lines[0])


if __name__ == "__main__":
    p1_ans = part1(deepcopy(lines))
    ans(p1_ans)  # 26984457539
    p2_ans = part2(deepcopy(lines))
    ans(p2_ans)  # 1741362314973
