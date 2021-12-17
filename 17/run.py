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


ints = lambda l: list(map(int, l))

############### end of boilerplate ############################################


### PART 1 ###


def parse_input():
    lines = data.strip().splitlines()
    print(f"{len(lines)} lines in {input_file}\n")
    nums = lines[0].split("target area: ")[1]
    xs, ys = nums.split(", ")
    x1, x2 = ints(xs.split("=")[1].split(".."))
    y1, y2 = ints(ys.split("=")[1].split(".."))
    goal_area = set()
    min_y = float("inf")
    max_x = float("-inf")
    for x in range(min(x1, x2), max(x1, x2) + 1):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            goal_area.add((x, y))
            min_y = min(y, min_y)
            max_x = max(x, max_x)
    return goal_area, max_x, min_y


def launch(velocities):
    """
    launch at some (velocity_x, velocity_y)
    return (success_bool, highest_y_val)
    """
    xvel, yvel = velocities
    x = y = 0
    highest = y
    while True:
        if (x, y) in goal_area:
            return True, highest
        else:
            x += xvel
            y += yvel
            highest = max(y, highest)
            # drag
            if x == 0:
                pass
            elif xvel > 0:
                xvel -= 1
            elif xvel < 0:
                xvel += 1
            # gravity
            yvel -= 1
        if y < min_y:
            # we're below the goal area
            return False, float("-inf")
        if x > max_x:
            # we're past the goal area horizontally
            return False, float("-inf")


if __name__ == "__main__":
    goal_area, max_x, min_y = parse_input()
    best_highpoint = float("-inf")
    successful_launches = set()
    # tried to watch the output and choose well-bounded ranges
    # given my input of
    #   target area: x=119..176, y=-141..-84
    #                 max_x__/       \__min_y
    for xvel in range(0, max_x + 1):
        for yvel in range(min_y - 1, 1000):
            hit, height = launch((xvel, yvel))
            if hit:
                successful_launches.add((xvel, yvel))
                print("hit!", (xvel, yvel), height)
                if height > best_highpoint:
                    best_highpoint = height
                    print("new record!", (xvel, yvel), best_highpoint)
    print("(part 1) Highest point reached:")
    ans(best_highpoint)  # 9870
    print("(part 2) Number of distinct (xvel, yvel) that hit:")
    ans(len(successful_launches))  # 5523
    # runs in about 5 seconds
