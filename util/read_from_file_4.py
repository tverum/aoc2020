def read_passports(filename: str) -> list:
    """
    Read the passports from file
    :param filename: the filename
    :return: a list of dicts containing the passport
    """
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file.readlines()]

    passports = []
    current_passport = {}
    for line in lines:
        if not line:
            passports.append(current_passport)
            current_passport = {}
        else:
            fields = line.split()
            current_passport.update({field.split(":")[0]: field.split(":")[1] for field in fields})

    if current_passport:
        passports.append(current_passport)
        current_passport = {}

    return passports
