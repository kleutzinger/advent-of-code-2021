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


############### end of boilerplate ###################################################

line_groups = data.split("\n\n")
print(f"{len(lines)} lines in {input_file}\n")


def count_pairs(string):
    counts = Counter()
    for idx in range(len(string) - 1):
        pair = string[idx] + string[idx + 1]
        counts[pair] += 1
    return counts


def insert_slow(string, rules):
    """
    the slow way I originally did it, which operated on strings.
    "NNCB" -> "NCNBHB"
    """
    nu_str = ""
    for idx in range(len(string) - 1):
        pair = string[idx] + string[idx + 1]
        nu_str += pair[0] + rules[pair]
    return nu_str + pair[1]


def insert(pair_counts, rules, char_counter):
    """
    here we have a pair_counts where we keep track of the frequency of pairs
    in the polymer. {NN: 1, NC: 4, ...}

    and the global amounts of each individual character {N: 5, B: 200, ...}
    """
    next_pair_counts = Counter()
    for pair, cur_pair_count in pair_counts.items():
        nu_chr = rules[pair]
        # we have the pair frequency. so we're adding that many nu_chr
        char_counter[nu_chr] += cur_pair_count
        # add to left pair _N
        next_pair_counts[pair[0] + nu_chr] += cur_pair_count
        # add to right pair N_
        next_pair_counts[nu_chr + pair[1]] += cur_pair_count
    return next_pair_counts, char_counter


def most_minus_least(char_counter):
    """
    we take the count of individual characters subtract the least common from
    the most common
    """
    freqs = list(char_counter.most_common())
    most, least = freqs[0], freqs[-1]
    print(f"{most=}, {least=}")
    return most[1] - least[1]


def part12():
    polymer, insertions = line_groups
    polymer = polymer.strip().splitlines()[0]
    insertions = [i.split(" -> ") for i in insertions.strip().splitlines()]
    rules = {pair: nu_chr for pair, nu_chr in insertions}
    pair_counts = count_pairs(polymer)
    char_counter = Counter(polymer)
    for round in range(40):
        pair_counts, char_counter = insert(pair_counts, rules, char_counter)
        if round == 9:
            print("part 1:")
            ans(most_minus_least(char_counter))  # 2657
    print("part 2:")
    ans(most_minus_least(char_counter))  # 2911561572630


if __name__ == "__main__":
    part12()
