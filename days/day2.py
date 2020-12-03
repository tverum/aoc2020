from util.read_from_file_2 import read_passwords_file


def check_password_1(line: tuple) -> bool:
    l_range, letter, password = line
    min, max = l_range
    return min <= password.count(letter) <= max


def check_password_2(line: tuple) -> bool:
    l_range, letter, password = line
    min, max = l_range

    check_1 = password[min - 1] == letter
    check_2 = password[max - 1] == letter
    return check_1 != check_2


def day_2():
    filename = "./inputs/day/2.txt"
    passwords = read_passwords_file(filename)
    if not passwords:
        print("main -- There was a problem reading the passwords file")
        exit(-1)

    n_correct_pw = sum([check_password_1(pw) for pw in passwords])
    print("day 2 -- RESULTAAT 1: {}".format(n_correct_pw))

    n_correct_pw = sum([check_password_2(pw) for pw in passwords])
    print("day 2 -- RESULTAAT 2: {}".format(n_correct_pw))
    exit(0)
