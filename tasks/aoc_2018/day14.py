from main import data_path

DATA = data_path(__file__)


def puzzle1() -> None:
    number = 920831

    scoreboard = [3, 7]
    elf1 = 0
    elf2 = 1

    def get_div(index, start=True):
        if index == elf1:
            result = "(" if start else ")"
        elif index == elf2:
            result = "[" if start else "]"
        else:
            result = " "

        return result

    def print_board():
        print(
            "".join(
                "{}{}{}".format(get_div(i), e, get_div(i, False)) for i, e in enumerate(scoreboard)
            )
        )

    print_board()
    while True:
        if len(scoreboard) >= 10 + number:
            break

        new_recipe = scoreboard[elf1] + scoreboard[elf2]

        if new_recipe < 10:
            scoreboard.append(new_recipe)
        else:
            scoreboard.append(new_recipe // 10)
            scoreboard.append(new_recipe % 10)

        elf1 = (elf1 + 1 + scoreboard[elf1]) % len(scoreboard)
        elf2 = (elf2 + 1 + scoreboard[elf2]) % len(scoreboard)

    # print_board()
    print("".join(map(str, scoreboard[-10:])))


def puzzle2() -> None:
    target = "920831"

    scoreboard = "37"

    elf1 = 0
    elf2 = 1
    while target not in scoreboard[-7:]:
        scoreboard += str(int(scoreboard[elf1]) + int(scoreboard[elf2]))
        elf1 = (elf1 + int(scoreboard[elf1]) + 1) % len(scoreboard)
        elf2 = (elf2 + int(scoreboard[elf2]) + 1) % len(scoreboard)

    # print_board()
    print(scoreboard.index(target))
