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

table = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}

example1 = "110100101111111000101000"
# ----------VVVTTTAAAAABBBBBCCCCC


def parse_input():
    """ """
    lines = data.strip().splitlines()
    print(f"{len(lines)} lines in {input_file}\n")
    line_groups = data.strip().split("\n\n")  # lines split by double newlines
    parsed = ""
    for idx, c in enumerate(lines[0]):
        parsed += table[c]

    pprint(parsed)
    print(f"{len(parsed)=}")
    return parsed


b2i = lambda n: int(n, 2)

LITERAL = 4


def parse_literal(value):
    head = 0
    build = ""
    groups_parsed = 0
    while True:
        leader = value[head]
        tail = value[head + 1 : head + 5]
        build += tail
        groups_parsed += 1
        if leader == "0":
            return b2i(build), groups_parsed * 5
            break
        head += 5
    return b2i(build), bits_parsed


def parse_packet(packet):
    version = b2i(packet[:3])
    type_id = b2i(packet[3:6])
    rest = packet[6:]
    if type_id == LITERAL:
        p, jmp = parse_literal(rest)
    else:  # OPERATOR
        lti = rest[0]
        if lti == "0":
            length = b2i(rest[1:16])

            # the length of subpackets
            pass
        elif lti == "1":
            num_sub_packets = b2i(rest[1:12])

        """
        
        If the length type ID is 0, then the next 15 bits are a number that
        represents the total length in bits of the sub-packets contained by
        this packet.

        If the length type ID is 1, then the next 11 bits are a number that
        represents the number of sub-packets immediately contained by this
        packet.

        """

    pass


example2 = "00111000000000000110111101000101001010010001001000000000"
# ----------VVVTTTILLLLLLLLLLLLLLLAAAAAAAAAAABBBBBBBBBBBBBBBB

# print(parse_packet(example1))
print(parse_packet(example2))
print(parse_packet("11010001010"))
exit()


def part12(data):
    tot = 0
    for idx, d in enumerate(data):
        if d:
            tot += 1
    return tot


if __name__ == "__main__":
    data = parse_input()
    part12(deepcopy(data))
