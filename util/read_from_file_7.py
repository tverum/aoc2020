import re

SUBJECT_PATTERN = '(^\S+ \S+)'
ALLOWED_PATTERN = "((\d+) (\S+ \S+) (bag|bags))"


def read_rules(filename: str) -> dict:
    """
    Read the answers for day 7
    :param filename: the filename containing the answers
    :return: a list of answers
    """
    with open(filename, 'r') as file:
        lines = file.readlines()

    rules = {}
    for line in lines:
        subject = re.match(SUBJECT_PATTERN, line).group(1)
        allowed = [(match.group(2), match.group(3)) for match in re.finditer(ALLOWED_PATTERN, line)]
        rules[subject] = allowed

    return rules
