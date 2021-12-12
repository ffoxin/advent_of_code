from collections import defaultdict, Counter
from pathlib import Path
from typing import List

DATA = (Path(__file__).parent / "data" / (Path(__file__).stem + ".txt")).read_text()


def puzzle1():
    entries = list(filter(bool, DATA.split("\n")))
    links = defaultdict(set)
    for line in entries:
        start, end = line.split("-")
        links[start].add(end)
        links[end].add(start)

    def find_path(path: List[str]) -> List[List[str]]:
        next_nodes = [
            node for node in links[path[-1]] if node.isupper() or node not in path
        ]
        found_paths: List[List[str]] = []
        for node in next_nodes:
            if node == "end":
                found_paths.append(path + [node])
            else:
                found_paths.extend(find_path(path + [node]))

        return found_paths

    results = find_path(["start"])
    for result in results:
        print("-".join(result))
    print(len(results))


def puzzle2():
    entries = list(filter(bool, DATA.split("\n")))
    links = defaultdict(set)
    for line in entries:
        start, end = line.split("-")
        if end != "start":
            links[start].add(end)
        if start != "start":
            links[end].add(start)

    def find_path(path: List[str]) -> List[List[str]]:
        next_nodes = [
            node
            for node in links[path[-1]]
            if node.isupper()
            or node not in path
            or Counter(filter(str.islower, path)).most_common(1)[0][1] < 2
        ]
        found_paths: List[List[str]] = []
        for node in next_nodes:
            if node == "end":
                found_paths.append(path + [node])
            else:
                found_paths.extend(find_path(path + [node]))

        return found_paths

    results = find_path(["start"])
    # results = set(map(lambda x: '-'.join(x), results))
    for result in results:
        print(",".join(result))
    print(len(results))


if __name__ == "__main__":
    try:
        puzzle2()
    except NameError as e:
        if str(e) != "name 'puzzle2' is not defined":
            raise
        puzzle1()
