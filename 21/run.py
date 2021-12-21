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


def parse_input():
    lines = data.strip().splitlines()
    p1_start = int(lines[0].split("position: ")[1])
    p2_start = int(lines[1].split("position: ")[1])
    return p1_start, p2_start


def part12(data):
    pos1, pos2 = data
    score1 = score2 = 0
    num_rolls = 0

    def check_win(s1, s2) -> bool:
        "check for ending of part 1"
        print("part 1:")
        if s1 >= 1000:
            print(f"{s1, s2}{s2 * num_rolls=}")
            ans(s2 * num_rolls)
            return True
        if s2 >= 1000:
            print(f"{s1, s2}{s1 * num_rolls=}")
            ans(s1 * num_rolls)
            return True
        return False  # no winner

    def add_mod(n, plus, modulo=10):
        """
        add `plus` to `n` with a one-indexed modulo
        """
        n += plus
        return ((n - 1) % modulo) + 1

    die = 100
    p2turn = False
    while not check_win(score1, score2):
        if p2turn == False:  # p1 turn
            for _ in range(3):
                die = add_mod(die, 1, 100)
                pos1 = add_mod(pos1, die)
                print(pos1, die)
            score1 += pos1
        elif p2turn == True:  # p2 turn
            for _ in range(3):
                die = add_mod(die, 1, 100)
                pos2 = add_mod(pos2, die)
                print(die)
            score2 += pos2
        p2turn = not p2turn
        num_rolls += 3
        print(f"{(pos1, score1)=}, {(pos2, score2)=}")


if __name__ == "__main__":
    data = parse_input()
    part12(deepcopy(data))
