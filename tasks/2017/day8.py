import re
from collections import defaultdict

from main import data_path

DATA = data_path(__file__)


def puzzle1():
    with open(DATA, "r") as f:
        lines = f.readlines()

    template = re.compile(r"(\w+) (inc|dec) (-?\d+) if (\w+) ([<>=!]+) (-?\d+)")
    regs = defaultdict(int)
    for line in lines:
        a = template.match(line.strip())
        reg, op, val, reg_cond, op_cond, val_cond = a.groups()

        ival_cond = int(val_cond)
        ireg_cond = regs[reg_cond]
        if op_cond == ">=":
            if not (ireg_cond >= ival_cond):
                continue
        elif op_cond == ">":
            if not (ireg_cond > ival_cond):
                continue
        elif op_cond == "<=":
            if not (ireg_cond <= ival_cond):
                continue
        elif op_cond == "==":
            if not (ireg_cond == ival_cond):
                continue
        elif op_cond == "!=":
            if not (ireg_cond != ival_cond):
                continue
        elif op_cond == "<":
            if not (ireg_cond < ival_cond):
                continue
        else:
            raise RuntimeError("Unexpected op_cond", op_cond)

        ival = int(val)
        if op == "dec":
            ival *= -1

        regs[reg] += ival

    print(max(regs.values()))


def puzzle2():
    with open(DATA, "r") as f:
        lines = f.readlines()

    template = re.compile(r"(\w+) (inc|dec) (-?\d+) if (\w+) ([<>=!]+) (-?\d+)")
    regs = defaultdict(int)
    result = 0
    for line in lines:
        a = template.match(line.strip())
        reg, op, val, reg_cond, op_cond, val_cond = a.groups()

        ival_cond = int(val_cond)
        ireg_cond = regs[reg_cond]
        if op_cond == ">=":
            if not (ireg_cond >= ival_cond):
                continue
        elif op_cond == ">":
            if not (ireg_cond > ival_cond):
                continue
        elif op_cond == "<=":
            if not (ireg_cond <= ival_cond):
                continue
        elif op_cond == "==":
            if not (ireg_cond == ival_cond):
                continue
        elif op_cond == "!=":
            if not (ireg_cond != ival_cond):
                continue
        elif op_cond == "<":
            if not (ireg_cond < ival_cond):
                continue
        else:
            raise RuntimeError("Unexpected op_cond", op_cond)

        ival = int(val)
        if op == "dec":
            ival *= -1

        regs[reg] += ival
        result = max(result, regs[reg])

    print(result)
