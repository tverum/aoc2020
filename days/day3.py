import math

from util.read_from_file_3 import read_slope

angles = [
    (1, 1),
    (1, 3),
    (1, 5),
    (1, 7),
    (2, 1)
]


def day_3():
    filename = "./inputs/day/3.txt"
    multiplier = max(map(lambda angle: angle[1], angles))
    slope = read_slope(filename, multiplier)
    if not slope:
        print("main -- There was a problem reading the slope file")
        exit(-1)

    angle = (1, 3)
    result = check_slope(slope, angle)
    print("day 3 -- RESULTAAT 1: {}".format(result))

    result = 1
    for angle in angles:
        hits = check_slope(slope, angle)
        result *= hits

    print("day 3 -- RESULTAAT 2: {}".format(result))


    exit(0)


def check_slope(slope: list, angle: tuple):
    # determine how many times we have to go down
    iterations = math.ceil(len(slope)/angle[0])
    hits = sum([slope[angle[0] * i][angle[1] * i] == '#' for i in range(iterations)])
    return hits
