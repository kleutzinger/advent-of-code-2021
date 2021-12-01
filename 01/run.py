import os
import sys
import shutil
from itertools import chain, combinations
from copy import deepcopy

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

def line_transform(line):
    # split = [line.split() for line in lines]
    # return int(line)
    return int(line)


lines = [line_transform(line) for line in lines]  # apply line_transform to each line
s = list(sorted(lines))
max_ = max(lines)
min_ = min(lines)
mid = s[len(s)//2]

incs = 0
for idx, line in enumerate(lines):
    if idx == 0:
        last = line
        continue
    if line > last:
        incs += 1
    last = line

# not 98, 101
ans(incs) # 1532


#### Part 2 ####

sums = []
for idx, line in enumerate(lines):
    if idx >= len(lines) - 2:
        print('skip')
        continue
    s = lines[idx] + lines[idx+1]+ lines[idx+2]

    sums.append(s)
print(len(sums), len(lines))
    
    
incs = 0
for idx, line in enumerate(sums):
    if idx == 0:
        last = line
        continue
    if line > last:
        incs += 1
    last = line

# not 1458
# not 1482
# not 1569
ans(incs) #1571
