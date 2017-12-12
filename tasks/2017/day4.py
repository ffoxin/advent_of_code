from main import data_path

DATA = data_path(__file__)


def puzzle1():
    with open(DATA, 'r') as f:
        lines = f.readlines()

    def is_valid(line):
        words = line.split()
        return len(words) == len(set(words))

    result = sum(map(is_valid, lines))
    print(result)


def puzzle2():
    with open(DATA, 'r') as f:
        lines = f.readlines()

    def is_valid(line):
        words = line.split()
        words_set = set(''.join(sorted(word)) for word in words)
        return len(words) == len(words_set)

    result = sum(map(is_valid, lines))
    print(result)
