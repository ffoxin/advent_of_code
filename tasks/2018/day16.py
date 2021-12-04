from main import data_path

DATA = data_path(__file__)


def puzzle1():
    with open(DATA, "r") as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]

    r = [0, 0, 0, 0]

    def addr(a, b, c):
        r[c] = r[a] + r[b]

    def addi(a, b, c):
        r[c] = r[a] + b

    def mulr(a, b, c):
        r[c] = r[a] * r[b]

    def muli(a, b, c):
        r[c] = r[a] * b

    def banr(a, b, c):
        r[c] = r[a] & r[b]

    def bani(a, b, c):
        r[c] = r[a] & b

    def borr(a, b, c):
        r[c] = r[a] | r[b]

    def bori(a, b, c):
        r[c] = r[a] | b

    def setr(a, _, c):
        r[c] = r[a]

    def seti(a, _, c):
        r[c] = a

    def gtir(a, b, c):
        r[c] = int(a > r[b])

    def gtri(a, b, c):
        r[c] = int(r[a] > b)

    def gtrr(a, b, c):
        r[c] = int(r[a] > r[b])

    def eqir(a, b, c):
        r[c] = int(a == r[b])

    def eqri(a, b, c):
        r[c] = int(r[a] == b)

    def eqrr(a, b, c):
        r[c] = int(r[a] == r[b])

    ops = (
        addr,
        addi,
        mulr,
        muli,
        banr,
        bani,
        borr,
        bori,
        setr,
        seti,
        gtir,
        gtri,
        gtrr,
        eqir,
        eqri,
        eqrr,
    )

    count = 0
    for before, asm, after, _ in zip(*[iter(lines)] * 4):
        if not before.startswith("Before"):
            break

        before = [int(i) for i in before[9:-1].split(",")]
        asm = [int(i) for i in asm.split(" ")]
        after = [int(i) for i in after[9:-1].split(",")]
        print(before)

        noted = 0
        for op in ops:
            r = list(before)
            op(*asm[1:])
            if r == after:
                noted += 1
        if noted >= 3:
            count += 1

    print(count)


def puzzle2():
    with open(DATA, "r") as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]

    r = [0, 0, 0, 0]

    def addr(a, b, c):
        r[c] = r[a] + r[b]

    def addi(a, b, c):
        r[c] = r[a] + b

    def mulr(a, b, c):
        r[c] = r[a] * r[b]

    def muli(a, b, c):
        r[c] = r[a] * b

    def banr(a, b, c):
        r[c] = r[a] & r[b]

    def bani(a, b, c):
        r[c] = r[a] & b

    def borr(a, b, c):
        r[c] = r[a] | r[b]

    def bori(a, b, c):
        r[c] = r[a] | b

    def setr(a, _, c):
        r[c] = r[a]

    def seti(a, _, c):
        r[c] = a

    def gtir(a, b, c):
        r[c] = int(a > r[b])

    def gtri(a, b, c):
        r[c] = int(r[a] > b)

    def gtrr(a, b, c):
        r[c] = int(r[a] > r[b])

    def eqir(a, b, c):
        r[c] = int(a == r[b])

    def eqri(a, b, c):
        r[c] = int(r[a] == b)

    def eqrr(a, b, c):
        r[c] = int(r[a] == r[b])

    ops = (
        addr,
        addi,
        mulr,
        muli,
        banr,
        bani,
        borr,
        bori,
        setr,
        seti,
        gtir,
        gtri,
        gtrr,
        eqir,
        eqri,
        eqrr,
    )

    op_codes = {i: set(ops) for i in range(len(ops))}

    for before, asm, after, _ in zip(*[iter(lines)] * 4):
        if not before.startswith("Before"):
            break

        before = [int(i) for i in before[9:-1].split(",")]
        asm = [int(i) for i in asm.split(" ")]
        after = [int(i) for i in after[9:-1].split(",")]

        for op in ops:
            r = list(before)
            op(*asm[1:])
            if r != after:
                op_codes[asm[0]] -= {op}

    for i in range(len(ops)):
        for key, value in op_codes.items():
            if len(value) == 1:
                for k, v in op_codes.items():
                    if k != key:
                        op_codes[k] -= value

    for key, value in op_codes.items():
        op_codes[key] = list(value)[0]

    program = lines[3106:]
    r = [0, 0, 0, 0]

    for asm in program:
        asm = [int(i) for i in asm.split(" ")]
        op_codes[asm[0]](*asm[1:])

    print(r[0])
