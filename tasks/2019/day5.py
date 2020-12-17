from pathlib import Path
from typing import List

DATA = (Path(__file__).parent / 'data' / 'day5.txt').read_text()


def execute(program: List[int], input_value) -> List[int]:
    ip = 0

    def interpret_value(index):
        opcode = program[ip]
        value = program[ip + index]
        mode = (opcode // (10 ** (index + 2 - 1))) % 10
        if mode == 0:
            result = program[value]
        else:
            result = value
        return result

    while True:
        op = program[ip] % 100
        if op == 1:
            value1, value2 = interpret_value(1), interpret_value(2)
            addr = program[ip + 3]
            program[addr] = value1 + value2
            print('[{:04x}] {:4} <- {:<2}(+) {:4} {:4}'.format(
                addr, program[addr], op, value1, value2
            ))
            ip += 4
        elif op == 2:
            value1, value2 = interpret_value(1), interpret_value(2)
            addr = program[ip + 3]
            program[addr] = value1 * value2
            print('[{:04x}] {:4} <- {:<2}(*) {:4} {:4}'.format(
                addr, program[addr], op, value1, value2,
            ))
            ip += 4
        elif op == 3:
            addr = program[ip + 1]
            program[addr] = input_value
            print('[{:04x}] {:4} <- {:<2}(in)'.format(
                addr, program[addr], op,
            ))
            ip += 2
        elif op == 4:
            value = interpret_value(1)
            print('[{:04x}] {:4} -> {:<2}(out)'.format(
                0, value, op,
            ))
            print(value)
            ip += 2
        elif op == 5:
            if interpret_value(1) != 0:
                ip = interpret_value(2)
            else:
                ip += 3
        elif op == 6:
            if interpret_value(1) == 0:
                ip = interpret_value(2)
            else:
                ip += 3
        elif op == 7:
            value1, value2 = interpret_value(1), interpret_value(2)
            addr = program[ip + 3]
            program[addr] = 1 if (value1 < value2) else 0
            print('[{:04x}] {:4} <- {:<2}(<) {:4} {:4}'.format(
                addr, program[addr], op, value1, value2,
            ))
            ip += 4
        elif op == 8:
            value1, value2 = interpret_value(1), interpret_value(2)
            addr = program[ip + 3]
            program[addr] = 1 if (value1 == value2) else 0
            print('[{:04x}] {:4} <- {:<2}(=) {:4} {:4}'.format(
                addr, program[addr], op, value1, value2,
            ))
            ip += 4
        elif op == 99:
            break
        else:
            raise RuntimeError('Unsupported opcode: {}'.format(op))

    return program


def puzzle1():
    entries = [i for i in DATA.split('\n') if i]

    program = list(map(int, entries[0].split(',')))

    result = execute(program, 1)


def puzzle2():
    entries = [i for i in DATA.split('\n') if i]

    program = list(map(int, entries[0].split(',')))

    execute(program, 5)


if __name__ == '__main__':
    try:
        puzzle2()
    except NameError as e:
        if str(e) != "name 'puzzle2' is not defined":
            raise
        puzzle1()
