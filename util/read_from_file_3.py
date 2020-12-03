def read_slope(filename: str, multiplier: int) -> list:
    """
    Read the mountain slope from the file
    :param filename: the filename
    :return: a matrix containing the slope
    """
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file.readlines()]

    slope_length = len(lines)
    repeat = int((slope_length / len(lines[-1])) * multiplier) + 1
    slope = [
        [point for point in (line * repeat)] for line in lines
    ]
    return slope
