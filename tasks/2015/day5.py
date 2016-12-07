vowels = 'aeiou'
forbidden = ['ab', 'cd', 'pq', 'xy']


def condition1(s):
    return sum([s.count(vowel) for vowel in vowels]) >= 3


def condition2(s):
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return True
    return False


def condition3(s):
    return not any([sub in s for sub in forbidden])


def is_nice(s):
    return condition1(s) and condition2(s) and condition3(s)


def condition_more_1(s):
    for i in range(len(s) - 1):
        sub = s[i] + s[i + 1]
        if sub in s[i + 2:]:
            return True
    return False


def condition_more_2(s):
    for i in range(len(s) - 2):
        if s[i] == s[i + 2]:
            return True
    return False


def is_more_nice(s):
    return condition_more_1(s) and condition_more_2(s)


def puzzle1():
    data = 'tasks/2015/data/day5.txt'

    with open(data, 'r') as f:
        print(sum(map(is_nice, f.readlines())))


def puzzle2():
    data = 'tasks/2015/data/day5.txt'

    with open(data, 'r') as f:
        print(sum(map(is_more_nice, f.readlines())))
