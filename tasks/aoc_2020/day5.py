from pathlib import Path

DATA = (Path(__file__).parent / "data" / "day5.txt").read_text()


def get_seat_id(code: str):
    row_code = code[:7]
    col_code = code[7:]
    row = 0
    for i, letter in enumerate(reversed(row_code)):
        if letter == "B":
            row += 2**i
    col = 0
    for i, letter in enumerate(reversed(col_code)):
        if letter == "R":
            col += 2**i
    seat_id = row * 8 + col
    # print(row_code, col_code)
    # print(row, col)
    # print(seat_id)
    return row, col, seat_id


def decode_seat(seat_id: int):
    row = seat_id % 8
    col = seat_id / 8
    return row, col, seat_id


def puzzle1() -> None:
    entries = [i for i in DATA.split("\n") if i]
    seats = [get_seat_id(entry)[2] for entry in entries]
    print(max(seats))


def puzzle2() -> None:
    entries = [i for i in DATA.split("\n") if i]
    seats = frozenset([get_seat_id(entry) for entry in entries])
    cols = frozenset([seat[0] for seat in seats])
    rows = frozenset([seat[1] for seat in seats])
    seat_ids = frozenset([seat[2] for seat in seats])
    extreme_cols = frozenset([min(cols), max(cols)])
    extreme_rows = frozenset([min(rows), max(rows)])
    for seat_id in range(max(seat_ids)):
        row, col, _ = decode_seat(seat_id)
        if (
            seat_id not in seat_ids
            and seat_id - 1 in seat_ids
            and seat_id + 1 in seat_ids
            and row not in extreme_rows
            and col not in extreme_cols
        ):
            print(seat_id)


if __name__ == "__main__":
    try:
        puzzle2()
    except NameError as e:
        if str(e) != "name 'puzzle2' is not defined":
            raise
        puzzle1()
