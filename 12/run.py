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
    g = defaultdict(set)
    for idx, line in enumerate(data):
        a, b = line.split("-")
        g[a].add(b)
        g[b].add(a)
    seen_small = set()
    paths = set()

    def valid_path(path):
        c = Counter(path)
        if c["start"] > 1:
            return False
        if c["end"] > 1:
            return False
        seen_two = False
        for k, val in c.items():
            if k.upper() == k:
                continue
            if val > 2:
                return False
            if val > 1:
                if seen_two:
                    return False
                seen_two = True
        return True

    def dfs(root, path=tuple()):
        nonlocal seen_small
        if root == "end":
            final_path = path + (root,)
            if valid_path(final_path):  # why did this fix it?
                paths.add(final_path)
            return
        # kinda commented out part 1
        # for neighb in g[root]:
        #     if neighb not in path  or neighb.upper() == neighb:
        #         seen_small.add(neighb)
        #         dfs(neighb, path + (root,))
        for neighb in sorted(g[root]):
            if valid_path(path + (neighb,)):
                dfs(neighb, path + (root,))

    dfs("start")
    # pt 2 not 4448, 222559

    return len(paths)


if __name__ == "__main__":
    # part 1: 4167
    # part 2: 98441
    ans(part12(deepcopy(lines)))
