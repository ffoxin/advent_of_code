from itertools import chain
from pathlib import Path
from typing import List, Set

DATA = (Path(__file__).parent / "data" / (Path(__file__).stem + ".txt")).read_text()


class Card:
    SIZE = 5

    def __init__(self, lines: List[str]) -> None:
        self._data: List[int] = []
        for line in lines:
            for item in line.split():
                self._data.append(int(item))
        self._marked: Set[int] = set()

    def mark(self, value: int):
        if value in self._data:
            self._marked.add(value)

    def check(self):
        return any(
            chain(
                [
                    all(
                        item in self._marked
                        for item in self._data[row * self.SIZE : (row + 1) * self.SIZE]
                    )
                    for row in range(self.SIZE)
                ],
                [
                    all(item in self._marked for item in self._data[col :: self.SIZE])
                    for col in range(self.SIZE)
                ],
            )
        )

    def get_sum(self):
        return sum(i for i in self._data if i not in self._marked)

    def __repr__(self) -> str:
        return "\n".join(
            [
                "".join(
                    f'{"[" if item in self._marked else " "}{item:>2d}{"]" if item in self._marked else " "}'
                    for item in self._data[i * self.SIZE : (i + 1) * self.SIZE]
                )
                for i in range(self.SIZE)
            ]
        )


def puzzle1() -> None:
    entries = list(filter(bool, DATA.split("\n")))
    assert (len(entries) - 1) % Card.SIZE == 0, f"Unexpected number of entries: {len(entries)}"

    draw = list(map(int, entries[0].split(",")))
    cards = [
        Card(entries[i * Card.SIZE + 1 : (i + 1) * Card.SIZE + 1])
        for i in range((len(entries) - 1) // 5)
    ]

    winner = None

    for i in draw:
        for card in cards:
            card.mark(i)
        for card_index, card in enumerate(cards):
            if card.check():
                winner = (card_index, i)
        if winner is not None:
            break

    print(f"Winner: {winner[0] + 1} with {winner[1]}")
    print(f"Result: {cards[winner[0]].get_sum() * winner[1]}")


def puzzle2() -> None:
    entries = list(filter(bool, DATA.split("\n")))
    assert (len(entries) - 1) % Card.SIZE == 0, f"Unexpected number of entries: {len(entries)}"

    draw = list(map(int, entries[0].split(",")))
    cards = [
        (True, Card(entries[i * Card.SIZE + 1 : (i + 1) * Card.SIZE + 1]))
        for i in range((len(entries) - 1) // 5)
    ]

    winner = None
    valid_cards = len(cards)
    for step, i in enumerate(draw):
        for valid, card in cards:
            if valid:
                card.mark(i)

        for card_index, (valid, card) in enumerate(cards):
            if valid and card.check():
                valid_cards -= 1
                cards[card_index] = (False, card)
                winner = (card_index, i)

        if valid_cards == 0:
            break

    print(f"Winner: {winner[0] + 1} with {winner[1]}")
    print(f"Result: {cards[winner[0]][1].get_sum() * winner[1]}")


if __name__ == "__main__":
    try:
        puzzle2()
    except NameError as e:
        if str(e) != "name 'puzzle2' is not defined":
            raise
        puzzle1()
