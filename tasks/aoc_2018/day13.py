from enum import unique, Enum, auto
from itertools import cycle
from operator import attrgetter

from main import data_path

DATA = data_path(__file__)


@unique
class Move(Enum):
    Left = auto()
    Down = auto()
    Right = auto()
    Up = auto()

    def left(self):
        return Move(((self.value - 1) + 1) % 4 + 1)

    def right(self):
        return Move(((self.value - 1) - 1) % 4 + 1)


@unique
class Dir(Enum):
    Hor = auto()
    Vert = auto()
    Any = auto()
    Diag = auto()
    RevDiag = auto()
    Crash = auto()


class Cell:
    def __init__(self, ch):
        if ch in "^v|":
            self.dir = Dir.Vert
        elif ch in "<>-":
            self.dir = Dir.Hor
        elif ch == "+":
            self.dir = Dir.Any
        elif ch == "/":
            self.dir = Dir.Diag
        elif ch == "\\":
            self.dir = Dir.RevDiag

    def __str__(self):
        if self.dir == Dir.Vert:
            return "|"
        elif self.dir == Dir.Hor:
            return "-"
        elif self.dir == Dir.Any:
            return "+"
        elif self.dir == Dir.Diag:
            return "/"
        elif self.dir == Dir.RevDiag:
            return "\\"
        elif self.dir == Dir.Crash:
            return "X"


class Cart:
    def __init__(self, x, y, ch):
        self.x = x
        self.y = y
        self.turn = self.next_turn()
        if ch == "^":
            self.move = Move.Up
        elif ch == "v":
            self.move = Move.Down
        elif ch == "<":
            self.move = Move.Left
        elif ch == ">":
            self.move = Move.Right

    def __str__(self):
        if self.move == Move.Up:
            return "^"
        elif self.move == Move.Down:
            return "v"
        elif self.move == Move.Right:
            return ">"
        elif self.move == Move.Left:
            return "<"

    @staticmethod
    def next_turn():
        for i in cycle((Move.Left, Move.Up, Move.Right)):
            yield i

    def tick(self, cell: Cell):
        if cell.dir == Dir.Any:
            next_turn = next(self.turn)
            if next_turn == Move.Left:
                self.move = self.move.l_value()
            elif next_turn == Move.Right:
                self.move = self.move.r_value()
        elif cell.dir == Dir.Diag:
            if self.move in (Move.Up, Move.Down):
                self.move = self.move.r_value()
            elif self.move in (Move.Right, Move.Left):
                self.move = self.move.l_value()
        elif cell.dir == Dir.RevDiag:
            if self.move in (Move.Up, Move.Down):
                self.move = self.move.l_value()
            elif self.move in (Move.Right, Move.Left):
                self.move = self.move.r_value()

        if self.move == Move.Right:
            self.x += 1
        elif self.move == Move.Left:
            self.x -= 1
        elif self.move == Move.Up:
            self.y -= 1
        elif self.move == Move.Down:
            self.y += 1


def puzzle1() -> None:
    with open(DATA, "r") as f:
        lines = f.readlines()

    lines = [line.strip("\n") for line in lines]
    height = len(lines)
    width = max(map(len, lines))

    field = {}
    carts = {}
    for y, line in enumerate(lines):
        for x, ch in enumerate(line):
            if ch == " ":
                continue
            field[(x, y)] = Cell(ch)
            if ch in "<>^v":
                carts[(x, y)] = Cart(x, y, ch)

    def print_field():
        for y in range(height):
            line = []
            for x in range(width):
                point = (x, y)
                if point in carts:
                    line.append(str(carts[point]))
                elif point in field:
                    line.append(str(field[point]))
                else:
                    line.append(" ")
            print("".join(line))

    point = None
    while True:
        crash = False
        for cart in sorted(carts.values(), key=attrgetter("y", "x")):
            point = (cart.x, cart.y)
            cart.tick(field[point])
            carts.pop(point)
            point = (cart.x, cart.y)
            if point in carts:
                carts.pop(point)
                field[point].dir = Dir.Crash
                crash = True
                break
            carts[point] = cart
        if crash:
            break

    print(",".join(map(str, point)))


def puzzle2() -> None:
    with open(DATA, "r") as f:
        lines = f.readlines()

    lines = [line.strip("\n") for line in lines]
    height = len(lines)
    width = max(map(len, lines))

    field = {}
    carts = {}
    for y, line in enumerate(lines):
        for x, ch in enumerate(line):
            if ch == " ":
                continue
            field[(x, y)] = Cell(ch)
            if ch in "<>^v":
                carts[(x, y)] = Cart(x, y, ch)

    def print_field():
        for y in range(height):
            line = []
            for x in range(width):
                point = (x, y)
                if point in carts:
                    line.append(str(carts[point]))
                elif point in field:
                    line.append(str(field[point]))
                else:
                    line.append(" ")
            print("".join(line))

    # print_field()
    while True:
        crash = False
        for cart in sorted(carts.values(), key=attrgetter("y", "x")):
            point = (cart.x, cart.y)
            if point not in carts:
                continue
            cart.tick(field[point])
            carts.pop(point)
            point = (cart.x, cart.y)
            if point in carts:
                carts.pop(point)
                if len(carts) == 1:
                    crash = True
            else:
                carts[point] = cart
        if crash:
            break
        # print_field()
    # print_field()

    point = list(carts.keys())[0]
    print(",".join(map(str, point)))
