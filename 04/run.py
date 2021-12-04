import os
import shutil
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


def coords(arr2d):
    # return [(x0,y0), (x1, y0), ...]
    for y in range(len(arr2d)):
        for x in range(len(arr2d[y])):
            yield (x, y)

############### end of boilerplate ############################################


### PART 1 ###


def line_transform(line):
    "I run on each line of the input"
    # split = [line.split() for line in lines]
    # return int(line)
    return line

lines = [line_transform(line) for line in lines]

called = [int(i) for i in lines[0].strip().split(',')]
print(called)

def check_win(board):
    # cols
    for row in board:
        if all([marked for val, marked in row]):
            return True
    for row in list(map(list, zip(*board))):
        if all([marked for val, marked in row]):
            return True
    return False



def mark(board, num):
    for x, y in coords(board):
        if board[y][x][0] == num:
            board[y][x] = (board[y][x][0], True)
    return board

def line2nums(line):
    pass


def make_boards():
    boards = []
    for part in data.split('\n\n')[1:]:
        cur_board = []
        for line in part.strip().split('\n'):
            cur_row = []
            for num in line.replace('  ', ' ').strip().split(' '):
                print(line)
                try:
                    num = int(num)
                    cur_row.append((num, False))
                except:
                    pass
            cur_board.append(deepcopy(cur_row))
        boards.append(deepcopy(cur_board))
    return boards


def score(board):
    tot = 0
    for x, y in coords(board):
        val, marked = board[y][x]
        if not marked:
            tot += val
    return tot

def part1(lines):
    boards = make_boards()
    for board in boards:
        print(board)
    for call in called:
        for idx, board in enumerate(boards):
            boards[idx] = mark(board, call)
            if check_win(boards[idx]):
                return score(board) * call


### PART 2 ###


def part2(lines):
    boards = make_boards()
    i_won = [False] * len(boards)
    for board in boards:
        print(board)
    for call in called:
        for idx, board in enumerate(boards):
            if i_won[idx]:
                continue
            boards[idx] = mark(board, call)
            if check_win(boards[idx]):
                i_won[idx] = True
                if all(i_won):
                    print(score(boards[idx]), call)
                    return score(boards[idx]) * call



if __name__ == "__main__":
    p1_ans = part1(deepcopy(lines))
    # not 928
    ans(p1_ans) # 12796
    p2_ans = part2(deepcopy(lines))
    ans(p2_ans) # 18063
