from pathlib import Path

DATA = (Path(__file__).parent / "data" / (Path(__file__).stem + ".txt")).read_text()


class Point:
    def __init__(self):
        self.x = 0
        self.y = 0

    def R(self):
        self.x += 1

    def L(self):
        self.x -= 1

    def U(self):
        self.y += 1

    def D(self):
        self.y -= 1

    def __str__(self):
        return f"[{self.x}, {self.y}]"


class Tail(Point):
    def __init__(self, head: Point):
        super().__init__()
        self.head = head
        self.visited = {(0, 0)}
        self.max_x = 0
        self.min_x = 0
        self.max_y = 0
        self.min_y = 0

    def move(self):
        need_move: bool = abs(self.head.x - self.x) > 1 or abs(self.head.y - self.y) > 1
        if need_move:
            if self.head.x == self.x:
                assert abs(self.head.y - self.y) == 2
                self.y = (self.head.y + self.y) // 2
            elif self.head.y == self.y:
                assert abs(self.head.x - self.x) == 2
                self.x = (self.head.x + self.x) // 2
            elif abs(self.head.x - self.x) == 1:
                assert abs(self.head.y - self.y) == 2
                self.x = self.head.x
                self.y = (self.head.y + self.y) // 2
            elif abs(self.head.y - self.y) == 1:
                assert abs(self.head.x - self.x) == 2
                self.x = (self.head.x + self.x) // 2
                self.y = self.head.y
            elif abs(self.head.x - self.x) == 2 or abs(self.head.y - self.y) == 2:
                # for part 2 only
                assert abs(self.head.x - self.x) == 2
                assert abs(self.head.y - self.y) == 2
                self.x = (self.head.x + self.x) // 2
                self.y = (self.head.y + self.y) // 2
            else:
                raise RuntimeError(
                    f"Unexpected state: head[{str(self.head)}] tail[{str(self)}]"
                )

            self.visited.add((self.x, self.y))

            self.min_x = min(self.min_x, self.head.x, self.x)
            self.max_x = max(self.max_x, self.head.x, self.x)

            self.min_y = min(self.min_y, self.head.y, self.y)
            self.max_y = max(self.max_y, self.head.y, self.y)

    def R(self):
        self.move()

    def L(self):
        self.move()

    def U(self):
        self.move()

    def D(self):
        self.move()

    def print(self):
        for y in range(self.max_y, self.min_y - 1, -1):
            line = []
            for x in range(self.min_x, self.max_x + 1):
                if (x, y) == (self.head.x, self.head.y):
                    line.append("H")
                elif (x, y) == (self.x, self.y):
                    line.append("T")
                elif (x, y) == (0, 0):
                    line.append("s")
                elif (x, y) in self.visited:
                    line.append("#")
                else:
                    line.append(".")
            print("".join(line))


def puzzle1():
    entries = list(filter(bool, DATA.split("\n")))

    head = Point()
    tail = Tail(head)
    for line in entries:
        move, count = line.split(" ")
        assert len(move) == 1
        assert count.isdigit()
        count = int(count)

        for _ in range(count):
            getattr(head, move)()
            getattr(tail, move)()

    print(len(tail.visited))


def puzzle2():
    entries = list(filter(bool, DATA.split("\n")))
    head = Point()
    tails = [head]
    for _ in range(9):
        tails.append(Tail(tails[-1]))

    for line in entries:
        move, count = line.split(" ")
        assert len(move) == 1
        assert count.isdigit()
        count = int(count)

        for _ in range(count):
            for tail in tails:
                getattr(tail, move)()

    print(len(tails[-1].visited))


if __name__ == "__main__":
    try:
        puzzle2()
    except NameError as e:
        if str(e) != "name 'puzzle2' is not defined":
            raise
        puzzle1()
