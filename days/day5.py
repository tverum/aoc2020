from util.read_from_file_5 import read_boarding_passes


def determine_proper_bp(boarding_pass_ids, max_value):
    """
    Determine own boarding pass id
    :param boarding_pass_ids: the list of boarding pass ids
    :param max_value: the maximum value of the ids
    :return: the value that is missing
    """
    for i in range(max_value):
        if (i - 1 in boarding_pass_ids) and (i + 1 in boarding_pass_ids) and (not (i in boarding_pass_ids)):
            return i


def day_5():
    filename = "./inputs/day/5.txt"
    boarding_pass_ids = read_boarding_passes(filename)

    if not boarding_pass_ids:
        print("main -- There was a problem reading the boarding passes")
        exit(-1)

    result = max(boarding_pass_ids)
    print("day 5 -- RESULTAAT 1: {}".format(result))

    result = determine_proper_bp(boarding_pass_ids, result)
    print("day 5 -- RESULTAAT 2: {}".format(result))