from itertools import product
from typing import List

from main import data_path

DATA = data_path(__file__)


def execute(program: List[int]) -> List[int]:
    ip = 0
    while True:
        cmd = program[ip]
        if cmd == 1:
            program[program[ip + 3]] = program[program[ip + 1]] + program[program[ip + 2]]
            ip += 4
        elif cmd == 2:
            program[program[ip + 3]] = program[program[ip + 1]] * program[program[ip + 2]]
            ip += 4
        elif cmd == 99:
            break

    return program


def puzzle1() -> None:
    with open(DATA) as f:
        int_code = list(map(int, f.read().split(",")))

    assert execute([1, 0, 0, 0, 99]) == [2, 0, 0, 0, 99], execute([1, 0, 0, 0, 99])
    assert execute([2, 3, 0, 3, 99]) == [2, 3, 0, 6, 99], execute([2, 3, 0, 3, 99])
    assert execute([2, 4, 4, 5, 99, 0]) == [2, 4, 4, 5, 99, 9801], execute([2, 4, 4, 5, 99, 0])
    assert execute([1, 1, 1, 4, 99, 5, 6, 0, 99]) == [
        30,
        1,
        1,
        4,
        2,
        5,
        6,
        0,
        99,
    ], execute([1, 1, 1, 4, 99, 5, 6, 0, 99])

    int_code[1] = 12
    int_code[2] = 2
    execute(int_code)

    print(int_code[0])


def puzzle2() -> None:
    with open(DATA) as f:
        int_code = list(map(int, f.read().split(",")))

    for i, j in product(range(100), range(100)):
        program_copy = list(int_code)
        program_copy[1] = i
        program_copy[2] = j

        execute(program_copy)

        if program_copy[0] == 19690720:
            print(i * 100 + j)
            return

    print("nothing found")
