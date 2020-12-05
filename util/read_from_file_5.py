def translate_bp_to_id(bp: str) -> int:
    """
    Translate a boarding pass to its ID
    :param bp: the boarding pass
    :return: an integer containing the boarding pass
    """
    bp = bp.replace('R', '1').\
        replace('L', '0').\
        replace('F', '0').\
        replace('B', '1')

    id = -1
    try:
        id = int(bp, base=2)
    except ValueError:
        print("util/read_from_file_5 -- The values provided were not all integers")
        exit(-1)

    return id


def read_boarding_passes(filename: str) -> list:
    """
    Read the boarding passes (day 5) from a file defined by filename
    :param filename: the name of the file
    :return: a list with the boarding passes
    """
    with open(filename, 'r') as file:
        passes = file.readlines()

    passes = [translate_bp_to_id(bp.strip()) for bp in passes]
    return passes