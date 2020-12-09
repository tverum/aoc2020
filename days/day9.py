from itertools import product
from pprint import pprint

from util.read_from_file_9 import read_numbers

WINDOW_SIZE = 25


def find_wrong_number(numbers: list) -> int:
    """
    Find the first number in the list that does not hold to the property
    :param numbers: the list of numbers
    :return: the first number that does not hold to the property
    """
    window = numbers[:WINDOW_SIZE]
    index = WINDOW_SIZE
    while index < len(numbers):
        combinations = list(product(window, repeat=2))
        combinations = list(map(lambda x: x[0] + x[1], combinations))
        if not numbers[index] in combinations:
            return numbers[index]
        else:
            window = window[1:]
            window.append(numbers[index])
            index += 1

    return -1


def find_contiguous_set(numbers: list, invalid_number: int) -> int:
    """
    Find the contiguous set of numbers that add up to the invalid number
    :param numbers: the list of numbers
    :param invalid_number: the number that was deduced to be invalid
    :return: the weakness in the encryption (sum of smallest and biggest number of the contiguous set)
    """
    index = 0
    tmp_index = index
    tmp_list = []
    accumulator = 0
    while index < len(numbers):
        while accumulator < invalid_number:
            accumulator += numbers[tmp_index]
            tmp_list.append(numbers[tmp_index])
            tmp_index += 1
        if accumulator == invalid_number:
            return min(tmp_list) + max(tmp_list)
        else:
            index += 1
            tmp_index = index
            tmp_list = []
            accumulator = 0
    return -1


def day_9():
    filename = "./inputs/day/9.txt"
    numbers = read_numbers(filename)

    if not numbers:
        print("main -- There was a problem reading the numbers")
        exit(-1)

    result = find_wrong_number(numbers)
    print("day 9 -- RESULTAAT 1: {}".format(result))

    result = find_contiguous_set(numbers, result)
    print("day 9 -- RESULTAAT 2: {}".format(result))
