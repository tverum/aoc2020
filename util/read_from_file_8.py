import re

INSTRUCTION_PATTERN = '^(\S+) ((\+|-)\d+)'


def read_instructions(filename: str) -> list:
    """
    Read the instructions for day 8
    :param filename: the filename containing the instructions
    :return: a list of instructions
    """
    with open(filename, 'r') as file:
        lines = file.readlines()

    instructions = []
    for line in lines:
        match = re.match(INSTRUCTION_PATTERN, line)
        instructions.append((match.group(1), match.group(2)))

    return instructions
