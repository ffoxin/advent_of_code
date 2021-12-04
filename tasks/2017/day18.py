import enum

from main import data_path

DATA = data_path(__file__)


class Interrupt(Exception):
    def __init__(self, value):
        self.value = value


class OpResult(enum.Enum):
    Jump = enum.auto()
    Wait = enum.auto()
    Sent = enum.auto()


class Program:
    def __init__(self, p, lines):
        self.registers = {
            "ip": 0,
            "a": 0,
            "b": 0,
            "f": 0,
            "i": 0,
            "p": p,
        }

        self.program = []
        for line in lines:
            args = line.split(" ")
            cmd = args[0]
            if cmd == "snd":
                func = self.snd
            elif cmd == "set":
                if args[2].startswith("-") or args[2].isdigit():
                    func = self.set_number
                else:
                    func = self.set_register
            elif cmd == "add":
                if args[2].startswith("-") or args[2].isdigit():
                    func = self.add_number
                else:
                    func = self.add_register
            elif cmd == "mul":
                if args[2].startswith("-") or args[2].isdigit():
                    func = self.mul_number
                else:
                    func = self.mul_register
            elif cmd == "mod":
                if args[2].startswith("-") or args[2].isdigit():
                    func = self.mod_number
                else:
                    func = self.mod_register
            elif cmd == "rcv":
                func = self.rcv
            elif cmd == "jgz":
                if args[2].startswith("-") or args[2].isdigit():
                    func = self.jgz_number
                else:
                    func = self.jgz_register
            else:
                raise RuntimeError("unknown instruction: {}".format(cmd))
            self.program.append(func(*args[1:]))

    def snd(self, register):
        def wrapper():
            self.registers["snd"] = self.registers[register]

        return wrapper

    def set_number(self, register, value):
        def wrapper():
            self.registers[register] = int(value)

        return wrapper

    def set_register(self, register, value):
        def wrapper():
            self.registers[register] = self.registers[value]

        return wrapper

    def add_number(self, register, value):
        def wrapper():
            self.registers[register] += int(value)

        return wrapper

    def add_register(self, register, value):
        def wrapper():
            self.registers[register] += self.registers[value]

        return wrapper

    def mul_number(self, register, value):
        def wrapper():
            self.registers[register] *= int(value)

        return wrapper

    def mul_register(self, register, value):
        def wrapper():
            self.registers[register] *= self.registers[value]

        return wrapper

    def mod_number(self, register, value):
        def wrapper():
            self.registers[register] %= int(value)

        return wrapper

    def mod_register(self, register, value):
        def wrapper():
            self.registers[register] %= self.registers[value]

        return wrapper

    def rcv(self, register):
        def wrapper():
            if self.registers[register] != 0:
                raise Interrupt(self.registers["snd"])

        return wrapper

    def jgz_number(self, register, value):
        def wrapper():
            if self.registers[register] > 0:
                self.registers["ip"] += int(value)
                return OpResult.Jump

        return wrapper

    def jgz_register(self, register, value):
        def wrapper():
            if self.registers[register] > 0:
                self.registers["ip"] += self.registers[value]
                return OpResult.Jump

        return wrapper

    def execute(self):
        result = self.program[self.registers["ip"]]()
        if result != OpResult.Jump:
            self.registers["ip"] += 1

    def run(self):
        try:
            while True:
                self.execute()
        except Interrupt as e:
            return e.value


def puzzle1():
    with open(DATA, "r") as f:
        lines = f.readlines()

    lines = map(str.strip, lines)

    p = Program(0, lines)
    result = p.run()
    print(result)


class Program2(Program):
    def __init__(self, p, lines):
        super().__init__(p, lines)

        self.mq = []
        self.mq2 = None

    def set_mq(self, theirs_mq):
        self.mq2 = theirs_mq

    def snd(self, register):
        def wrapper():
            self.mq2.insert(0, self.registers[register])
            return OpResult.Sent

        return wrapper

    def rcv(self, register):
        def wrapper():
            if self.mq:
                self.registers[register] = self.mq.pop()
            else:
                return OpResult.Wait

        return wrapper

    def execute(self):
        result = self.program[self.registers["ip"]]()
        if result != OpResult.Jump:
            self.registers["ip"] += 1

        return result


def puzzle2():
    with open(DATA, "r") as f:
        lines = f.readlines()

    lines = list(map(str.strip, lines))

    p0 = Program2(0, lines)
    p1 = Program2(1, lines)
    p0.set_mq(p1.mq)
    p1.set_mq(p0.mq)

    send_count = 0
    try:
        while True:
            result0 = p0.execute()
            result1 = p1.execute()

            if result1 == OpResult.Sent:
                send_count += 1
            if result0 == result1 == OpResult.Wait:
                raise Interrupt(send_count)
    except Interrupt as e:
        return e.value
