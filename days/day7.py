from util.read_from_file_7 import read_rules

BAG_TYPE = 'shiny gold'


def contains_bag(current_bag_type: str, requested_bag_type: str, rules: dict) -> bool:
    """
    Check if the current bag allows the requested bag type
    :param current_bag_type: the current bag type to search from
    :param requested_bag_type: the requested bag type
    :param rules: the dict with the rules
    :return: a bool that determines if the requested_bag_type can be reached from here
    """
    allowed_bags = [rt[1] for rt in rules[current_bag_type]]
    if requested_bag_type in allowed_bags:
        return True
    for bt in allowed_bags:
        if contains_bag(bt, requested_bag_type, rules):
            return True
    return False


def number_of_bags(current_bag_type: str, rules: dict) -> int:
    """
    Calculate the number of bags in the current bag
    :param current_bag_type: the current node in the search tree
    :param rules: the dict with the rules
    :return: an integer containing the number of bags in the current node
    """
    allowed_bags = [rt[1] for rt in rules[current_bag_type]]
    multipliers = [int(rt[0]) for rt in rules[current_bag_type]]
    if not allowed_bags:
        return 1
    else:
        result = sum([multiplier * number_of_bags(ab, rules) for (ab, multiplier) in zip(allowed_bags, multipliers)])
        return result + 1


def day_7():
    filename = "./inputs/day/7.txt"
    rules = read_rules(filename)

    if not rules:
        print("main -- There was a problem reading the rules")
        exit(-1)

    result = sum([contains_bag(bag_type, BAG_TYPE, rules) for bag_type in rules])
    print("day 7 -- RESULTAAT 1: {}".format(result))

    result = number_of_bags(BAG_TYPE, rules) - 1
    print("day 7 -- RESULTAAT 2: {}".format(result))
