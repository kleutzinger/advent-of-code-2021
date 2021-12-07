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


############### end of boilerplate ############################################


### PART 1 ###


def pos_moves(nums, p):
    moves = 0
    for num in nums:
        moves += abs(p - num)
    return moves


def part1(nums):
    return min([pos_moves(nums, m) for m in range(min(nums), max(nums) + 1)])


def pos_moves2(nums, p):
    moves = 0

    def sgn(a, b):
        if a == b:
            return 0
        if a < b:
            return 1
        else:
            return -1

    for num in nums:
        cost = 1
        while num != p:
            num += sgn(num, p)
            moves += cost
            cost += 1
    return moves


def part2(nums):
    return min([pos_moves2(nums, m) for m in range(min(nums), max(nums) + 1)])


### PART 2 ###


if __name__ == "__main__":
    data = [int(i) for i in lines[0].split(",")]
    ans(part1(data.copy()))  # 342641
    ans(part2(data.copy()))  # 93006301
