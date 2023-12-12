from pathlib import Path
from typing import List, Callable, Tuple

DATA = (Path(__file__).parent / "data" / "day8.txt").read_text()


class Processor:
    def __init__(self, entries: List[str]):
        self.sp = 0
        self.accumulator = 0
        self.code: List[Tuple[Callable, int]] = []

        for entry in entries:
            op, arg = entry.split(" ")
            arg = int(arg)
            if op == "acc":
                func = self.acc
            elif op == "jmp":
                func = self.jmp
            elif op == "nop":
                func = self.nop
            else:
                raise NotImplementedError()
            self.code.append((func, arg))

    def acc(self, arg: int):
        self.accumulator += arg
        self.sp += 1

    def jmp(self, arg: int):
        self.sp += arg

    def nop(self, _: int):
        self.sp += 1

    def execute(self):
        func, arg = self.code[self.sp]
        func(arg)


def puzzle1() -> None:
    entries = [i for i in DATA.split("\n") if i]

    proc = Processor(entries)
    sp = set()
    while True:
        sp.add(proc.sp)
        proc.execute()
        if proc.sp in sp:
            break
    print(proc.accumulator)


def puzzle2() -> None:
    entries = [i for i in DATA.split("\n") if i]

    proc = Processor(entries)
    found = False
    for index, (func, arg) in enumerate(proc.code):
        if func == proc.nop:
            new_func = proc.jmp
        elif func == proc.jmp:
            new_func = proc.nop
        else:
            continue

        proc.code[index] = (new_func, arg)

        proc.sp = 0
        proc.accumulator = 0
        sp = set()
        while True:
            sp.add(proc.sp)
            proc.execute()
            if proc.sp >= len(proc.code):
                found = True
                break
            if proc.sp in sp:
                break

        if found:
            break

        proc.code[index] = (func, arg)

    print(proc.accumulator)


if __name__ == "__main__":
    try:
        puzzle2()
    except NameError as e:
        if str(e) != "name 'puzzle2' is not defined":
            raise
        puzzle1()
