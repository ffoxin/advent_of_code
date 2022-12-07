from pathlib import Path
from typing import List, Dict

DATA = (Path(__file__).parent / "data" / (Path(__file__).stem + ".txt")).read_text()


class Node:
    def __init__(self, name: str):
        self.name = name

    def get_size(self) -> int:
        raise NotImplementedError()


class Dir(Node):
    ALL = []

    def __init__(self, name: str, parent: "Dir" = None):
        super().__init__(name)
        self.items: Dict[str, Node] = {}
        self.parent = parent
        self.__class__.ALL.append(self)

    def get_size(self) -> int:
        return sum(item.get_size() for item in self.items.values())

    def as_str(self, indent: int = 0) -> List[str]:
        result = []
        for name in sorted(self.items):
            content = self.items[name]
            if isinstance(content, Dir):
                result.append(f'{" " * indent * 2}- {name} (dir)')
                result.extend(content.as_str(indent + 1))
            else:
                assert isinstance(content, File)
                result.append(
                    f'{" " * indent * 2}- {content.name} (file, size={content.get_size()})'
                )

        return result


class File(Node):
    def __init__(self, name: str, size: int):
        super().__init__(name)
        self.size = size

    def get_size(self) -> int:
        return self.size


def parse_root() -> Dir:
    entries = list(filter(bool, DATA.split("\n")))

    root = Dir("/")
    current = root

    line_iter = iter(entries)

    while True:
        try:
            line = next(line_iter)
        except StopIteration:
            break

        parts = line.split(" ")

        if parts[0] == "$":
            cmd = parts[1]
            if cmd == "cd":
                target = parts[2]
                if target == "/":
                    continue
                if target == "..":
                    current = current.parent
                else:
                    assert target in current.items and isinstance(
                        current.items[target], Dir
                    ), f"directory {target} not found in {list(current.items.keys())}"
                    current = current.items[target]
            elif cmd == "ls":
                continue
            else:
                raise RuntimeError(f"Unexpected command: {cmd}")
        else:
            name = parts[1]
            if parts[0] == "dir":
                current.items[name] = Dir(name, current)
            else:
                size = int(parts[0])
                current.items[name] = File(name, size)

    return root


def puzzle1():
    parse_root()

    result = 0
    for item in Dir.ALL:
        size = item.get_size()
        if size <= 100_000:
            result += size

    print(result)


def puzzle2():
    parse_root()

    dir_sizes = [item.get_size() for item in Dir.ALL]

    dir_sizes = sorted(dir_sizes)
    total = dir_sizes[-1]
    for size in dir_sizes:
        if total - size < 70000000 - 30000000:
            print(size)
            break


if __name__ == "__main__":
    try:
        puzzle2()
    except NameError as e:
        if str(e) != "name 'puzzle2' is not defined":
            raise
        puzzle1()
