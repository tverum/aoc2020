def read_numbers(filename: str) -> list:
    """
    Read the numbers for day 9
    :param filename: the filename containing the numbers
    :return: a list of numbers
    """
    with open(filename, 'r') as file:
        lines = file.readlines()

    numbers = [int(line.strip()) for line in lines]

    return numbers
