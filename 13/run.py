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


line_groups = data.split("\n\n")  # lines split by double newlines
# line_groups = [l.strip() for l in line_groups]  # remove trailing newlines
# print(lines)
print(f"{len(lines)} lines in {input_file}\n")

############### end of boilerplate ############################################

### PART 1 and 2 ###


def max_dims(board):
    maxx, maxy = float("-inf"), float("-inf")
    for x, y in board.keys():
        maxx, maxy = max(maxx, x), max(maxy, y)
    return maxx, maxy


def show2d(board):
    max_x, max_y = max_dims(board)
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            draw_cell = (x, y)
            if board[draw_cell]:
                print("█", end="")
            else:
                print(" ", end="")
        print()


def do_fold(board, fold):
    axis, pivot = fold
    max_x, max_y = max_dims(board)
    nu_board = defaultdict(bool)
    if axis == "y":
        """
        0110
        0000
        ----
        0000
        0111
        """
        for dy in range(0, pivot + 1):
            below_y, above_y = pivot + dy, pivot - dy
            for y in range(max_x + 1):
                if board[(y, below_y)] or board[(y, above_y)]:
                    nu_board[(y, above_y)] = True
        print(len(nu_board.items()))
        return nu_board
    elif axis == "x":
        """
        01|10
        00|00
        00|00
        01|11
        """
        nu_board = defaultdict(bool)
        for dx in range(0, pivot + 1):
            left_x, right_x = pivot - dx, pivot + dx
            for y in range(max_y + 1):
                if board[(left_x, y)] or board[(right_x, y)]:
                    nu_board[(left_x, y)] = True
        print(len(nu_board.items()))
        return nu_board


def part12():
    coord_lines, fold_lines = line_groups
    dots = []
    for coord_line in coord_lines.split("\n"):
        a, b = coord_line.split(",")
        dots.append((int(a), int(b)))

    folds = []
    for fold in fold_lines.split("\n")[:-1]:
        axis = fold.split("=")[0][-1]
        mag = int(fold.split("=")[1])
        folds.append((axis, mag))

    board = defaultdict(bool)
    for coord in dots:
        board[coord] = True

    show2d(board)
    for fold in folds:
        board = do_fold(board, fold)  # 720 (part 1)
        show2d(board)
    # AHPRPAUZ (part 2)


"""
 ██  █  █ ███  ███  ███   ██  █  █ ████
█  █ █  █ █  █ █  █ █  █ █  █ █  █    █
█  █ ████ █  █ █  █ █  █ █  █ █  █   █ 
████ █  █ ███  ███  ███  ████ █  █  █  
█  █ █  █ █    █ █  █    █  █ █  █ █   
█  █ █  █ █    █  █ █    █  █  ██  ████
"""


if __name__ == "__main__":
    part12()
