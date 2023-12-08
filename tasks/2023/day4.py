import re
from collections import defaultdict
from pathlib import Path

DATA = (Path(__file__).parent / "data" / (Path(__file__).stem + ".txt")).read_text()

CARD_TEMPLATE = re.compile(r"Card\s+(\d+)")


def puzzle1():
    entries: list[str] = list(filter(bool, DATA.split("\n")))
    result: int = 0
    for line in entries:
        card: str
        numbers: str
        card, numbers = line.split(": ")
        wins: set[int]
        yours: set[int]
        wins, yours = map(lambda x: set(map(int, x.split())), numbers.split(" | "))
        win_factor: int = len(wins & yours)
        if win_factor:
            result += 2 ** (win_factor - 1)

    print(result)


def puzzle2():
    entries: list[str] = list(filter(bool, DATA.split("\n")))
    card_wins: dict[int, int] = {}
    for line in entries:
        card: str
        numbers: str
        card, numbers = line.split(": ")
        try:
            card_id: int = int(CARD_TEMPLATE.fullmatch(card).group(1))
        except Exception:
            raise RuntimeError(line)
        wins: set[int]
        yours: set[int]
        wins, yours = map(lambda x: set(map(int, x.split())), numbers.split(" | "))
        win_factor: int = len(wins & yours)
        card_wins[card_id] = win_factor

    instances: dict[int, int] = defaultdict(int)
    card_id: int
    win_factor: int
    for card_id, win_factor in card_wins.items():
        instances[card_id] += 1
        for i in range(win_factor):
            instances[card_id + i + 1] += instances[card_id]

    print(sum(instances.values()))


if __name__ == "__main__":
    try:
        puzzle2()
    except NameError as e:
        if str(e) != "name 'puzzle2' is not defined":
            raise
        puzzle1()
