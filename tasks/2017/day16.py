from main import data_path

DATA = data_path(__file__)


def puzzle1():
    with open(DATA, 'r') as f:
        lines = f.readlines()

    programs = [chr(i + ord('a')) for i in range(16)]

    # lines = ['s1,x3/4,pe/b']
    # programs = list('abcde')

    commands = lines[0].split(',')

    for command in commands[:50]:
        cmd, rest = command[0], command[1:]
        if cmd == 's':
            spin = int(rest)
            programs = programs[-spin:] + programs[:-spin]
        elif cmd == 'x':
            a, b = tuple(map(int, rest.split('/')))
            programs[a], programs[b] = programs[b], programs[a]
        elif cmd == 'p':
            pa, pb = rest.split('/')
            a = programs.index(pa)
            b = programs.index(pb)
            programs[a], programs[b] = programs[b], programs[a]

        print(command, ''.join(programs))


def puzzle2():
    with open(DATA, 'r') as f:
        lines = f.readlines()

    programs = [chr(i + ord('a')) for i in range(16)]
    starting = list(programs)

    # lines = ['s1,x3/4,pe/b']
    # programs = list('abcde')

    commands = lines[0].split(',')

    def spin(x):
        nonlocal programs
        programs = programs[-x:] + programs[:-x]

    def exchange(pos1, pos2):
        nonlocal programs
        programs[pos1], programs[pos2] = programs[pos2], programs[pos1]

    def partner(prog1, prog2):
        nonlocal programs
        exchange(programs.index(prog1), programs.index(prog2))

    cmd_list = []
    for command in commands:
        cmd, rest = command[0], command[1:]
        if cmd == 's':
            x = int(rest)
            cmd_list.append((spin, x))
        elif cmd == 'x':
            a, b = tuple(map(int, rest.split('/')))
            cmd_list.append((exchange, a, b))
        elif cmd == 'p':
            pa, pb = rest.split('/')
            cmd_list.append((partner, pa, pb))

    total = 1000000000
    rounds = -1
    for i in range(total):
        for cmd in cmd_list:
            cmd[0](*cmd[1:])
        if programs == starting:
            rounds = i + 1
            break

    if rounds != -1:
        rest = total % rounds
        for i in range(rest):
            for cmd in cmd_list:
                cmd[0](*cmd[1:])

    print(''.join(programs))
