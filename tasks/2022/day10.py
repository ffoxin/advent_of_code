from pathlib import Path

DATA = (Path(__file__).parent / "data" / (Path(__file__).stem + ".txt")).read_text()


def puzzle1():
    entries = list(filter(bool, DATA.split("\n")))

    x = 1
    cycle = 1
    rest = 0
    value = None
    line_iter = iter(entries)
    result = 0

    while True:

        if rest == 1:
            assert value is not None
            x += value

        if rest == 0:
            try:
                line = next(line_iter)
            except StopIteration:
                break

            if line == "noop":
                rest = 0
            else:
                assert line is not None
                op, value = line.split(" ")
                assert op == "addx"
                value = int(value)
                rest = 1
        else:
            rest -= 1

        cycle += 1
        if (cycle - 20) % 40 == 0 and cycle <= 220:
            result += cycle * x

    print(result)


def puzzle2():
    entries = list(filter(bool, DATA.split("\n")))

    screen = [" "] * 240
    sprite = {0, 1, 2}
    x = 1
    cycle = 0
    rest = 0
    value = None
    line_iter = iter(entries)

    while True:

        cycle += 1

        if cycle <= 240:
            # print(f'cycle  {(cycle - 1) // 40 + 1} ' + ''.join('?' if i + 1 == cycle else screen[i] for i in range(40)))
            # print(f'sprite {(x // 40) + 1} ' + ''.join('#' if i in sprite else '.' for i in range(40)))
            screen[cycle - 1] = "#" if (cycle - 1) % 40 in sprite else "."

        if rest == 0:
            try:
                line = next(line_iter)
            except StopIteration:
                break

            if line == "noop":
                rest = 0
            else:
                assert line is not None
                op, value = line.split(" ")
                assert op == "addx"
                value = int(value)
                rest = 1
        elif rest == 1:
            assert value is not None
            x += value
            sprite = {x - 1, x, x + 1}
            rest -= 1
        else:
            rest -= 1

        # print('crt    ' + ''.join(screen[:40]))
        # assert line is not None
        # print(f'{line}, cycle={cycle} x={x} rest={rest}')

    for i in range(6):
        print("".join(screen[i * 40 : (i + 1) * 40]))


if __name__ == "__main__":
    try:
        puzzle2()
    except NameError as e:
        if str(e) != "name 'puzzle2' is not defined":
            raise
        puzzle1()
