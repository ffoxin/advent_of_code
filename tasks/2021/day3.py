from pathlib import Path
from typing import List

DATA = (Path(__file__).parent / 'data' / 'day3.txt').read_text()


def puzzle1():
    entries = list(filter(bool, DATA.split('\n')))
    size = len(entries[0])
    print('size', size)

    bits = [0] * size
    for entry in entries:
        for index, char in enumerate(reversed(entry)):
            if char == '1':
                bits[index] += 1

    gamma = ''.join(reversed([str(int(2 * bits[i] > len(entries))) for i in range(size)]))
    epsilon = ''.join(reversed([str(int(2 * bits[i] <= len(entries))) for i in range(size)]))
    gamma = int(gamma, base=2)
    epsilon = int(epsilon, base=2)
    print(gamma * epsilon)


def puzzle2():
    entries = list(filter(bool, DATA.split('\n')))
    size = len(entries[0])
    print('size', size)

    def filter_list(data: List, comparator) -> int:
        for step in range(size):
            zeroes, ones = [], []
            for entry in data:
                (ones if entry[step] == '1' else zeroes).append(entry)
            data = ones if comparator(len(ones), len(zeroes)) else zeroes
            if len(data) == 1:
                break

        assert len(data) == 1, f'Data length expected 1, actual size "{len(data)}"'

        value = int(data[0], base=2)
        return value

    oxy = filter_list(entries, lambda x, y: x >= y)
    co2 = filter_list(entries, lambda x, y: x < y)
    print(oxy, co2)
    print(f'Result: {oxy * co2}')


if __name__ == '__main__':
    try:
        puzzle2()
    except NameError as e:
        if str(e) != "name 'puzzle2' is not defined":
            raise
        puzzle1()
