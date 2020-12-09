import copy

from util.read_from_file_8 import read_instructions

NOP_INSTRUCTION = 'nop'
ACC_INSTRUCTION = 'acc'
JMP_INSTRUCTION = 'jmp'


def execute_instruction(instruction, instruction_pointer, accumulator):
    """
    Execute a single instruction
    :param instruction: the instruction to be executed --> tuple
    :param instruction_pointer: the current instruction pointer
    :param accumulator: the current accumulator
    :return: the next instruction pointer, accumulator
    """
    if instruction[0] == NOP_INSTRUCTION:
        return instruction_pointer + 1, accumulator
    elif instruction[0] == ACC_INSTRUCTION:
        return instruction_pointer + 1, accumulator + int(instruction[1])
    elif instruction[0] == JMP_INSTRUCTION:
        return instruction_pointer + int(instruction[1]), accumulator
    else:
        print("main -- read invalid instruction")
        exit(-1)


def execute_reverse_instruction(instruction, instruction_pointer, accumulator):
    """
    Execute a single instruction in reverse
    :param instruction: the instruction to be executed --> tuple
    :param instruction_pointer: the current instruction pointer
    :param accumulator: the current accumulator
    :return: the next instruction pointer, accumulator
    """
    if instruction[0] == JMP_INSTRUCTION:
        return instruction_pointer + 1, accumulator
    elif instruction[0] == ACC_INSTRUCTION:
        return instruction_pointer + 1, accumulator + int(instruction[1])
    elif instruction[0] == NOP_INSTRUCTION:
        return instruction_pointer + int(instruction[1]), accumulator
    else:
        print("main -- read invalid instruction")
        exit(-1)


def follow_program_until_loop(instructions: list, instruction_pointer=0, accumulator=0, execution_order=None) -> tuple:
    """
    Follow the program until a duplicate instruction is met
    :param instructions: the list of instructions to follow
    :param instruction_pointer: the current instruction pointer
    :param accumulator: the current value of the accumulator
    :param execution_order: the current execution_order
    :return: tuple(did program finish, value of the accumulator)
    """
    if execution_order is None:
        execution_order = []
    program_length = len(instructions)

    while (instruction_pointer not in execution_order) and (instruction_pointer < program_length):
        execution_order.append(instruction_pointer)
        instruction_pointer, accumulator = execute_instruction(instructions[instruction_pointer], instruction_pointer,
                                                               accumulator)

    return (instruction_pointer == program_length), accumulator


def is_nop(instruction):
    """
    Check if an instruction is a nop
    :param instruction: the instruction (tuple)
    :return: true if the instruction is a NOP_instruction
    """
    return instruction[0] == NOP_INSTRUCTION


def is_jmp(instruction):
    """
    Check if an instruction is a jmp
    :param instruction: the instruction (tuple)
    :return: true if the instruction is a JMP_instruction
    """
    return instruction[0] == JMP_INSTRUCTION


def find_corrupt_instruction(instructions: list) -> int:
    """
    Follow the program and try changing nop <-> jmp until the program executes
    :param instructions: the list of instructions to follow
    :return: the value of the accumulator
    """
    instruction_pointer = 0
    accumulator = 0
    execution_order = []
    program_length = len(instructions)
    while (instruction_pointer not in execution_order) and (instruction_pointer < program_length):
        instruction = instructions[instruction_pointer]
        execution_order.append(instruction_pointer)
        if is_nop(instruction) or is_jmp(instruction):
            tmp_ip, tmp_acc = execute_reverse_instruction(instruction, instruction_pointer, accumulator)
            tmp_exo = copy.deepcopy(execution_order)
            finish, tent_acc = follow_program_until_loop(instructions, tmp_ip, tmp_acc, tmp_exo)
            if finish:
                return tent_acc
        instruction_pointer, accumulator = execute_instruction(instructions[instruction_pointer], instruction_pointer,
                                                               accumulator)

    print("main -- No solution found")
    exit(-1)


def day_8():
    filename = "./inputs/day/8.txt"
    instructions = read_instructions(filename)

    if not instructions:
        print("main -- There was a problem reading the instructions")
        exit(-1)

    _, result = follow_program_until_loop(instructions)
    print("day 7 -- RESULTAAT 1: {}".format(result))

    result = find_corrupt_instruction(instructions)
    print("day 7 -- RESULTAAT 1: {}".format(result))
