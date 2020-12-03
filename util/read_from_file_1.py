
def read_expense_report(filename: str) -> list:
    """
    Read the expense report (day 1) from a file defined by filename
    :param filename: the name of the file
    :return: a list with the expenses
    """
    with open(filename, 'r') as file:
        expenses = file.readlines()

    try:
        expenses = [int(expense) for expense in expenses]
    except ValueError:
        print("util/read_from_file1 -- The values provided were not all integers")
        return []

    return expenses
