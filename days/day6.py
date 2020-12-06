from pprint import pprint

from util.read_from_file_6 import read_answers


def distinct_answers(group):
    """
    Determine the distinct answers in a group
    :param group: the group containing lines of answers
    :return: the number of distinct answers in the group
    """
    distinct = set([])
    for line in group:

        distinct.update(line)

    return len(distinct)


def common_answers(group):
    pprint(group)
    common_set = set(group[0])
    for line in group[1:]:
        common_set = common_set.intersection(line)

    pprint(common_set)
    return len(common_set)


def day_6():
    filename = "./inputs/day/6.txt"
    groups = read_answers(filename)

    if not groups:
        print("main -- There was a problem reading the groups answers")
        exit(-1)

    result = sum([distinct_answers(group) for group in groups])
    print("day 6 -- RESULTAAT 1: {}".format(result))

    result = sum([common_answers(group) for group in groups])
    print("day 6 -- RESULTAAT 2: {}".format(result))