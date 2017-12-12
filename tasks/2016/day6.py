def analyze_file():
    data = 'tasks/data/day6.txt'
    freq = []
    with open(data, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            if len(freq) == 0:
                freq = [{} for _ in range(len(line))]
            for index, char in enumerate(line):
                if char in freq[index]:
                    freq[index][char] += 1
                else:
                    freq[index][char] = 1
    return freq


def puzzle1():
    freq = analyze_file()

    answer = ''
    for char in freq:
        stats = sorted(char, key=char.get)
        answer += stats[-1][0]

    print(answer)


def puzzle2():
    freq = analyze_file()

    answer = ''
    for char in freq:
        stats = sorted(char, key=char.get)
        answer += stats[0][0]

    print(answer)
