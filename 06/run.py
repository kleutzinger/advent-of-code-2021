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


def count_fish(nums=[], generations=80):
    """
    given a list of integers, find how many fish there are after X generations
    """
    fish = Counter(nums)
    for gen in range(generations):
        if "v" in sys.argv:
            print(gen, [(x, fish[x]) for x in range(9)])
        nu_fish = Counter()
        for idx in range(9):
            cur_count = fish[idx]
            if idx == 0:
                # spawn new fish
                nu_fish[8] += cur_count
                nu_fish[6] += cur_count
            else:
                # each fish -= 1 day
                nu_fish[idx - 1] += cur_count
        fish = nu_fish
    return sum(fish.values())


def part1(nums):
    return count_fish(nums, generations=80)


### PART 2 ###


def part2(nums):
    return count_fish(nums, generations=256)


if __name__ == "__main__":
    nums = [int(i) for i in lines[0].split(",")]
    p1_ans = part1(nums)
    ans(p1_ans)  # 26984457539
    p2_ans = part2(nums)
    ans(p2_ans)  # 1741362314973
