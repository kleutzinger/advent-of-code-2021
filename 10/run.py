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


### PART 1 and 2 ###


def part12(data):
    tot = 0
    m = {"}": "{", ")": "(", ">": "<", "]": "["}
    points = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }
    points2 = {
        "(": 1,
        "[": 2,
        "{": 3,
        "<": 4,
    }

    starts = m.values()
    ends = m.keys()
    tot = 0
    tot2s = []
    for idx, line in enumerate(data):
        tot2 = 0
        print(line)
        stack = []
        for c in line:
            if c in ends:
                top = stack.pop()
                print(c, top)
                if top != m[c]:
                    tot += points[c]
                    print(idx, "error", c, top)
                    break
            else:
                stack.append(c)
        else:
            print("SS", stack)
            for s in reversed(stack):
                tot2 *= 5
                tot2 += points2[s]
            tot2s.append(tot2)
            print(idx, "no error")
    tot2s.sort()
    ans(tot)  # 392139
    ans(tot2s[len(tot2s) // 2])  # 4001832844


if __name__ == "__main__":
    lines = [[c for c in line] for line in lines]
    part12(lines)
