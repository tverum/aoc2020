def read_answers(filename: str) -> list:
    """
    Read the answers for day 6
    :param filename: the filename containing the answers
    :return: a list of answers
    """
    with open(filename, 'r') as file:
        lines = file.readlines()

    groups = []
    current_group = []
    for line in lines:
        if line == '\n':
            groups.append(current_group)
            current_group = []
        else:
            current_group.append(line.strip())

    groups.append(current_group)

    return groups
