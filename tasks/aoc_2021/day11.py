from itertools import product
from pathlib import Path
from typing import List

DATA = (Path(__file__).parent / "data" / (Path(__file__).stem + ".txt")).read_text()


class Field:
    def __init__(self, entries: List[List[int]]) -> None:
        self.entries = entries
        self.flash_count = 0

    def inc(self, row: int, col: int) -> None:
        if not 0 <= row < len(self.entries):
            return
        if not 0 <= col < len(self.entries[0]):
            return
        self.entries[row][col] += 1

    def step(self) -> bool:
        self.entries = [[i + 1 for i in line] for line in self.entries]

        flashed = set()
        while True:
            last_size = len(flashed)
            for row, col in product(range(len(self.entries)), range(len(self.entries[0]))):
                if self.entries[row][col] > 9 and (row, col) not in flashed:
                    flashed.add((row, col))
                    self.flash_count += 1
                    self.entries[row][col] = 0
                    for i, j in product(range(-1, 2), repeat=2):
                        if (row + i, col + j) not in flashed:
                            self.inc(row + i, col + j)
            if last_size == len(flashed):
                break

        return len(flashed) == len(self.entries) * len(self.entries[0])

    def print(self):
        print("*" * 20)
        for line in self.entries:
            print("".join(map(str, line)))
        print("*" * 20)


def puzzle1() -> None:
    entries = list(map(lambda x: list(map(int, x)), filter(bool, DATA.split("\n"))))

    field = Field(entries)
    field.print()
    for i in range(100):
        field.step()
    field.print()
    print(f"Result: {field.flash_count}")


def puzzle2() -> None:
    entries = list(map(lambda x: list(map(int, x)), filter(bool, DATA.split("\n"))))

    field = Field(entries)
    step = 0
    while True:
        step += 1
        if field.step():
            break
    print(f"Result: {step}")


if __name__ == "__main__":
    try:
        puzzle2()
    except NameError as e:
        if str(e) != "name 'puzzle2' is not defined":
            raise
        puzzle1()
