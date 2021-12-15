from math import isnan
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

ref_big = """11637517422274862853338597396444961841755517295286
13813736722492484783351359589446246169155735727126
21365113283247622439435873354154698446526571955763
36949315694715142671582625378269373648937148475914
74634171118574528222968563933317967414442817852555
13191281372421239248353234135946434524615754563572
13599124212461123532357223464346833457545794456865
31254216394236532741534764385264587549637569865174
12931385212314249632342535174345364628545647573965
23119445813422155692453326671356443778246755488935
22748628533385973964449618417555172952866628316397
24924847833513595894462461691557357271266846838237
32476224394358733541546984465265719557637682166874
47151426715826253782693736489371484759148259586125
85745282229685639333179674144428178525553928963666
24212392483532341359464345246157545635726865674683
24611235323572234643468334575457944568656815567976
42365327415347643852645875496375698651748671976285
23142496323425351743453646285456475739656758684176
34221556924533266713564437782467554889357866599146
33859739644496184175551729528666283163977739427418
35135958944624616915573572712668468382377957949348
43587335415469844652657195576376821668748793277985
58262537826937364893714847591482595861259361697236
96856393331796741444281785255539289636664139174777
35323413594643452461575456357268656746837976785794
35722346434683345754579445686568155679767926678187
53476438526458754963756986517486719762859782187396
34253517434536462854564757396567586841767869795287
45332667135644377824675548893578665991468977611257
44961841755517295286662831639777394274188841538529
46246169155735727126684683823779579493488168151459
54698446526571955763768216687487932779859814388196
69373648937148475914825958612593616972361472718347
17967414442817852555392896366641391747775241285888
46434524615754563572686567468379767857948187896815
46833457545794456865681556797679266781878137789298
64587549637569865174867197628597821873961893298417
45364628545647573965675868417678697952878971816398
56443778246755488935786659914689776112579188722368
55172952866628316397773942741888415385299952649631
57357271266846838237795794934881681514599279262561
65719557637682166874879327798598143881961925499217
71484759148259586125936169723614727183472583829458
28178525553928963666413917477752412858886352396999
57545635726865674683797678579481878968159298917926
57944568656815567976792667818781377892989248891319
75698651748671976285978218739618932984172914319528
56475739656758684176786979528789718163989182927419
67554889357866599146897761125791887223681299833479
"""


### PART 1 ###


def parse_input(data):
    lines = data.strip().splitlines()
    print(f"{len(lines)} lines in {input_file}\n")
    line_groups = data.strip().split("\n\n")  # lines split by double newlines
    parsed = defaultdict(lambda: float("inf"))
    max_x = max_y = -1
    for y, line in enumerate(lines):
        for x, val in enumerate(line):
            max_x = max(x, max_x)
            max_y = max(y, max_y)
            parsed[(x, y)] = int(val)

    # pprint(parsed)
    # print(f"{len(parsed)=}")
    return parsed, (max_x, max_y)


def show2d(board, dims):
    max_x, max_y = dims
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            draw_cell = (x, y)
            print(board[draw_cell], end="")
        print("")


def neighbors(coord):
    x, y = coord
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        yield x + dx, y + dy


def part12(data, part2=True):
    from heapq import heappop, heappush

    board, max_dims = data
    max_dims2 = ((max_dims[0] + 1) * 5) - 1, ((max_dims[1] + 1) * 5) - 1
    print(max_dims, max_dims2)
    risk = 0
    x, y = (0, 0)
    seen = set([(0, 0)])
    Q = [(0, (0, 0))]

    def part2_risk(nbr):
        nonlocal board
        nx, ny = nbr
        # distance num offsets from top left
        if (nx < 0 or nx > max_dims2[0]) or (ny < 0 or ny > max_dims2[1]):
            return float("inf")
        offsets = 0
        x, y = nx, ny
        while x > max_dims[0]:
            x -= (max_dims[0] + 1)
            offsets += 1
        while y > max_dims[1]:
            y -= (max_dims[1] + 1)
            offsets += 1
        orig_risk = nu_risk = board[(x, y)]
        nu_risk += offsets
        nu_risk = (nu_risk - 1 ) % 9 + 1
        if isnan(nu_risk):
            breakpoint()
        return nu_risk
    
    for i in range(5):
        print(part2_risk((3, i*max_dims[0])))

    while True:
        risk, (x, y) = heappop(Q)
        if part2 and (x, y) == max_dims2:
            break
        if not part2 and (x, y) == max_dims:
            break
        # print(risk, x, y)
        for nbr in neighbors((x, y)):
            if nbr not in seen:
                if part2:
                    nbr_risk = risk + part2_risk(nbr)
                else:
                    nbr_risk = risk + board[nbr]
                if nbr_risk != float("inf"):
                    heappush(Q, (nbr_risk, nbr))
                seen.add(nbr)
        print(f"{(x,y, nbr_risk)=}")

        # pprint(Q)

    print("part 1:")
    ans(risk)


if __name__ == "__main__":
    parsed = parse_input(data)
    # print('mine:')
    # board, dims= to_big_board(parsed)
    # print(dims)
    # print('reference:')
    # board, dims = parse_input(ref_big)
    # print(dims)
    part12(deepcopy(parsed), part2=True)

    # not 2217
    # part12(deepcopy(to_big_board(parsed)))
