def read_passwords_file(filename: str) -> list:
    """
    Read the passwords file for day 2
    :param filename: the filename containing the passwords
    :return: a list of tuple of passwords and their policy
    """

    with open(filename, 'r') as file:
        lines = file.readlines()

    result = []
    for line in lines:
        result.append(read_password_line(line))

    return result


def read_password_line(line: str) -> tuple:
    """
    Read a single line of the password
    :param line: the single line to parse
    :return:
    """
    [l_range, letter, password] = line.split()
    l_range = get_range(l_range)
    letter = letter[0]
    return l_range, letter, password


def get_range(l_range: str) -> tuple:
    """
    Retrieve the integer range from the string
    :param l_range: the string version of the range
    :return:
    """
    try:
        [min, max] = [int(x) for x in l_range.split("-")]
    except ValueError:
        print("util/read_from_file2 -- Problem parsing the range")
    return min, max
