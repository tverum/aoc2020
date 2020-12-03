import itertools

from util.read_from_file_1 import read_expense_report


def fix_expense_report_1(expense_report: list) -> int:
    for expense_1, expense_2 in itertools.product(expense_report, repeat=2):
        if (expense_1 + expense_2) == 2020:
            return expense_1 * expense_2
    return -1


def fix_expense_report_2(expense_report: list) -> int:
    for expense_1, expense_2, expense_3 in itertools.product(expense_report, repeat=3):
        if (expense_1 + expense_2 + expense_3) == 2020:
            return expense_1 * expense_2 * expense_3
    return -1


def day_1():
    filename = "./inputs/day/1.txt"
    expense_report = read_expense_report(filename)
    if not expense_report:
        print("main -- There was a problem reading the expense report")
        exit(-1)

    result = fix_expense_report_1(expense_report)
    if result == -1:
        print("main -- No values found that add up to 2020")
        exit(-1)
    print("day 1 -- RESULTAAT 1: {}".format(result))

    result = fix_expense_report_2(expense_report)
    if result == -1:
        print("main -- No values found that add up to 2020")
        exit(-1)
    print("day 2 -- RESULTAAT 2: {}".format(result))
    exit(0)