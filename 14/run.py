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
    return line


lines = [line_transform(line) for line in lines]

if len(lines):
    l = lines[0]

try:
    nums = [int(i.strip()) for i in lines[0]]
except:
    pass


def pair_counts(temp):
    counts = Counter()
    for idx in range(len(temp) - 1):
        pair = temp[idx] + temp[idx + 1]
        counts[pair] += 1
    # counts[pair[1]+temp[-1]] += 1
    print(temp, counts)
    return counts


def round(temp, rules):
    nu_temp = ""
    for idx in range(len(temp) - 1):
        pair = temp[idx] + temp[idx + 1]
        nu_temp += pair[0] + rules[pair]
    return nu_temp + pair[1]


def round2(counts, rules, global_counter):
    nu_count = Counter()
    for pair, count in counts.items():
        nu_chr = rules[pair]
        global_counter[nu_chr] += count
        left = pair[0] + nu_chr
        right = nu_chr + pair[1]
        nu_count[left] += count
        nu_count[right] += count
    return nu_count, global_counter


def part1(data):
    temp, ins = line_groups
    temp = temp.strip().splitlines()[0]
    ins = ins.strip().splitlines()
    ins = [i.split(" -> ") for i in ins]
    rules = dict()
    for pair, chr in ins:
        rules[pair] = chr
    print(temp)
    print(pair_counts(temp))
    temp2 = pair_counts(temp)
    global_counter = Counter(temp)
    for r in range(40):
        # temp = round(temp, rules)
        temp2, global_counter = round2(temp2, rules, global_counter)
        print("global", global_counter)
        print(r)
        print(temp2)
        # print(pair_counts(temp))
    # pt 2 not 1290200791356
    c = list(temp2.most_common())
    print(c[0], c[-1])
    print(c[0][1] - c[-1][1])

    c = list(global_counter.most_common())
    print("part2:", c[0], c[-1])
    ans(c[0][1] - c[-1][1])
    # p2 not 3064796036668


if __name__ == "__main__":
    part1(data)
    # p2_ans = part2(deepcopy(lines))
    # ans(p2_ans)
