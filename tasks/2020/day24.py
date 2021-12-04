from operator import add
from pathlib import Path

DATA = (Path(__file__).parent / "data" / "day24.txt").read_text()

CHANGE = {
    "e": (2, 0),
    "w": (-2, 0),
    "se": (1, -2),
    "sw": (-1, -2),
    "ne": (1, 2),
    "nw": (-1, 2),
}


def get_coord(line):
    pos = 0
    tile = (0, 0)
    while pos < len(line):
        if line[pos] in "ew":
            change = CHANGE[line[pos]]
            pos += 1
        else:
            change = CHANGE[line[pos : pos + 2]]
            pos += 2
        tile = tuple(map(add, tile, change))

    return tile


def puzzle1():
    entries = [i for i in DATA.split("\n") if i]

    tiles = set()
    for entry in entries:
        tile = get_coord(entry)
        (tiles.remove if tile in tiles else tiles.add)(tile)

    print(len(tiles))


def puzzle2():
    entries = [i for i in DATA.split("\n") if i]

    tiles = set()
    for entry in entries:
        tile = get_coord(entry)
        (tiles.remove if tile in tiles else tiles.add)(tile)

    days = 100
    for _ in range(days):
        all_tiles = set()
        for tile in tiles:
            all_tiles.add(tile)
            all_tiles.update(
                [tuple(map(add, tile, change)) for change in CHANGE.values()]
            )
        new_tiles = set()
        for tile in all_tiles:
            neibs = sum(
                tuple(map(add, tile, change)) in tiles for change in CHANGE.values()
            )
            if neibs == 2 or tile in tiles and neibs == 1:
                new_tiles.add(tile)
        tiles = new_tiles

    print(len(tiles))


if __name__ == "__main__":
    try:
        puzzle2()
    except NameError as e:
        if str(e) != "name 'puzzle2' is not defined":
            raise
        puzzle1()
