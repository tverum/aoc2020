import re

from util.read_from_file_4 import read_passports

required_fields = [
    'byr',  # birth year
    'iyr',  # issue year
    'eyr',  # expiration year
    'hgt',  # height
    'hcl',  # hair color
    'ecl',  # eye color
    'pid',  # passport id
    'cid'  # country id
]

fixed_required_fields = [
    'byr',  # birth year
    'iyr',  # issue year
    'eyr',  # expiration year
    'hgt',  # height
    'hcl',  # hair color
    'ecl',  # eye color
    'pid',  # passport id
]

HEIGHT_PATTERN = "^(\d+)(cm|in)$"
HAIR_PATTERN = "^#(\d|[a-f]){6}$"
EYE_PATTERN = "^(amb|blu|brn|gry|grn|hzl|oth)$"
PASSPORT_PATTERN = "^\d{9}$"


def day_4():
    filename = "./inputs/day/4.txt"
    passports = read_passports(filename)

    if not passports:
        print("main -- There was a problem reading the slope file")
        exit(-1)

    result = check_required_fields(passports, 1)
    print("day 4 -- RESULTAAT 1: {}".format(result))

    result = check_required_fields(passports, 2)
    print("day 4 -- RESULTAAT 2: {}".format(result))


def check_required_fields(passports: list, assignment: int) -> int:
    """
    Check how many passports in the list have the required fields
    :param passports: the list of passports
    :return: a number of the amount of passports with the req. fields
    """
    if assignment == 1:
        return sum([1 for x in passports if all(elem in x.keys() for elem in fixed_required_fields)])
    else:
        return sum([1 for x in passports if all(elem in x.keys() for elem in fixed_required_fields) and valid_passport(x)])


def valid_passport(x: dict) -> bool:
    """
    Check if the passport is valid
    :param x: the passport
    :return: valid status of the passport (boolean)
    """
    cbyr = check_year(x['byr'], 1920, 2002)
    ciyr = check_year(x['iyr'], 2010, 2020)
    ceyr = check_year(x['eyr'], 2020, 2030)
    chgt = check_height(x['hgt'], HEIGHT_PATTERN)
    chcl = check_pattern(x['hcl'], HAIR_PATTERN)
    cecl = check_pattern(x['ecl'], EYE_PATTERN)
    cpid = check_pattern(x['pid'], PASSPORT_PATTERN)

    return all([cbyr, ciyr, ceyr, chgt, chcl, cecl, cpid])


def check_year(value: str, min: int, max: int) -> bool:
    """
    Check if the value of a year is correct
    :param value: the value that should contain a valid year
    :param min: the minimum year that is valid
    :param max: the maximum year that is valid
    :return: boolean indicating valid year
    """
    if not len(value) == 4:
        return False

    try:
        byr = int(value)
    except ValueError:
        return False
    else:
        return byr >= min and byr <= max


def check_height(value: str, pattern: str) -> bool:
    """
    Check if the height is valid
    :param value: the height in string
    :param pattern: the pattern that should match for the height
    :return: a boolean containing the valid status of the height
    """
    match = re.match(pattern, value)
    if not match:
        return False
    else:
        if match[2] == "in":
            return 59 <= int(match[1]) <= 76
        else:
            return 150 <= int(match[1]) <= 193


def check_pattern(value: str, pattern: str) -> bool:
    """
    Regex matching on patterns
    :param value: the value
    :param pattern: the pattern to be checked
    :return: boolean indicating valid pattern
    """
    return bool(re.match(pattern, value))
