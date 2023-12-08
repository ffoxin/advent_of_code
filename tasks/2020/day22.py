from pathlib import Path
from typing import Optional

DATA = (Path(__file__).parent / "data" / "day22.txt").read_text()


class Card:
    def __init__(self, value):
        self.value = value
        self.next = None


class Deck:
    def __init__(self):
        self.top_card: Optional[Card] = None
        self.bot_card: Optional[Card] = None

    def pop(self):
        card = self.top_card
        self.top_card = card.next
        return card

    def add_one(self, card: Card):
        if self.top_card is None:
            self.top_card = card
            self.bot_card = card
        else:
            self.bot_card.next = card
            self.bot_card = card
            card.next = None

    def add(self, card_win: Card, card_lose: Card):
        self.bot_card.next = card_win
        card_win.next = card_lose
        card_lose.next = None
        self.bot_card = card_lose

    def values(self):
        values = []
        next_card = self.top_card
        while next_card:
            values.append(next_card.value)
            next_card = next_card.next

        return values

    def copy(self, count):
        next_card = self.top_card
        deck = Deck()
        for _ in range(count):
            deck.add_one(Card(next_card.value))
            next_card = next_card.next
        return deck


def run_round(deck1: Deck, deck2: Deck):
    card1, card2 = deck1.pop(), deck2.pop()
    if card1.value > card2.value:
        deck1.add(card1, card2)
    else:
        deck2.add(card2, card1)

    return card1.value, card2.value


class GameCount:
    count = 0


class Game:
    def __init__(self, deck1: Deck, deck2: Deck):
        self.deck1 = deck1
        self.deck2 = deck2
        self.states = set()
        self.state1 = set()
        self.state2 = set()

        GameCount.count += 1
        self.game = GameCount.count

    def play(self):
        print("=== Game {} ===\n".format(self.game))

        rnd = 0
        while True:
            if self.deck1.top_card is None:
                winner = 2
                break
            if self.deck2.top_card is None:
                winner = 1
                break

            rnd += 1
            values1, values2 = (deck.values() for deck in (self.deck1, self.deck2))
            print("-- Round {} (Game {}) --".format(rnd, self.game))
            for index, values in enumerate((values1, values2), start=1):
                print("Player {} deck: {}".format(index, ", ".join(map(str, values))))

            # state = (tuple(values1), tuple(values2))
            # if state in self.states:
            #     print('HALT')
            #     return 1, values1
            # self.states.add(state)
            state1 = tuple(values1)
            state2 = tuple(values2)
            if state1 in self.state1 or state2 in self.state2:
                print("HALT")
                return 1, values1
            self.state1.add(state1)
            self.state2.add(state2)

            card1, card2 = self.deck1.pop(), self.deck2.pop()
            if card1.value < len(values1) and card2.value < len(values2):
                print("Playing a sub-game to determine the winner...\n")
                if max(values1[1 : card1.value + 1]) > max(
                    values2[1 : card2.value + 1]
                ):
                    winner = 1
                else:
                    winner, _ = Game(
                        self.deck1.copy(card1.value),
                        self.deck2.copy(card2.value),
                    ).play()
                print("...anyway, back to game {}.".format(self.game))
            else:
                if card1.value > card2.value:
                    winner = 1
                else:
                    winner = 2

            if winner == 1:
                self.deck1.add(card1, card2)
            else:
                self.deck2.add(card2, card1)

            print(
                "Player {} wins round {} of game {}!\n".format(winner, rnd, self.game)
            )

        return winner, (self.deck1 if winner == 1 else self.deck2).values()


def puzzle1():
    entries = [i for i in DATA.split("\n") if i]

    player_1_values = [int(i) for i in entries[1 : entries.index("Player 2:")]]
    player_2_values = [int(i) for i in entries[entries.index("Player 2:") + 1 :]]

    decks = []
    for values in (player_1_values, player_2_values):
        deck = Deck()
        for value in values:
            card = Card(value)
            if deck.top_card is None:
                deck.top_card = deck.bot_card = card
            else:
                deck.bot_card.next = card
                deck.bot_card = card
        decks.append(deck)

    rnd = 1
    while all(deck.top_card for deck in decks):
        print("-- Round {} --".format(rnd))
        for index, deck in enumerate(decks):
            print(
                "Player {} deck: {}".format(
                    index + 1, " ,".join(map(str, decks[index].values()))
                )
            )
        for index, value in enumerate(run_round(decks[0], decks[1])):
            print("Player {} plays: {}".format(index + 1, value))
        print("")
        rnd += 1

    # total_cards = sum(map(len, (player_1_values, player_2_values)))
    winner_deck = decks[0] if decks[0].top_card else decks[1]
    values = winner_deck.values()
    result = 0
    for index, value in enumerate(reversed(values), start=1):
        result += index * value
    print(result)


def puzzle23():
    entries = [i for i in DATA.split("\n") if i]

    player_1_values = [int(i) for i in entries[1 : entries.index("Player 2:")]]
    player_2_values = [int(i) for i in entries[entries.index("Player 2:") + 1 :]]

    deck1, deck2 = Deck(), Deck()
    for deck, values in ((deck1, player_1_values), (deck2, player_2_values)):
        for value in values:
            deck.add_one(Card(value))

    winner, values = Game(deck1, deck2).play()

    # print(winner, values)
    # 30685 too low
    # 31781 too low
    # 33928 incorrect
    # 33266 correct
    result = 0
    for index, value in enumerate(reversed(values), start=1):
        result += index * value
    print(result)


def puzzle2():
    deck1, deck2 = [i for i in DATA.split("\n\n")]
    deck1 = list(map(int, deck1.splitlines()[1:]))
    deck2 = list(map(int, deck2.splitlines()[1:]))

    def play_game(d1, d2):
        played = set()
        while True:
            if not d1:
                return 2, d2
            if not d2:
                return 1, d1

            state = (tuple(d1), tuple(d2))
            if state in played:
                return 1, d1
            played.add(state)

            if d1[0] < len(d1) and d2[0] < len(d2):
                nd1 = d1[1 : d1[0] + 1]
                nd2 = d2[1 : d2[0] + 1]
                if max(nd1) > max(nd2):
                    winner = 1
                else:
                    winner, _ = play_game(nd1, nd2)
            else:
                winner = 1 if d1[0] > d2[0] else 2

            if winner == 1:
                d1 = d1[1:] + [d1[0], d2[0]]
                d2 = d2[1:]
            else:
                d2 = d2[1:] + [d2[0], d1[0]]
                d1 = d1[1:]

    _, values = play_game(deck1, deck2)
    result = 0
    for index, value in enumerate(reversed(values), start=1):
        result += index * value
    print(result)


if __name__ == "__main__":
    try:
        puzzle2()
    except NameError as e:
        if str(e) != "name 'puzzle2' is not defined":
            raise
        puzzle1()
