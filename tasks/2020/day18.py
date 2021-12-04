import operator
from pathlib import Path
from typing import Optional, Callable

DATA = (Path(__file__).parent / "data" / "day18.txt").read_text()


def get_bracket_ranges(expr):
    bracket_range = []
    bracket_map = {}

    for index, item in enumerate(expr):
        if item == "(":
            bracket_range.append((index,))
        elif item == ")":
            for i in range(len(bracket_range) - 1, -1, -1):
                if len(bracket_range[i]) == 1:
                    bracket_range[i] = (bracket_range[i][0], index)
                    bracket_map[bracket_range[i][0]] = bracket_range[i]
                    bracket_map[bracket_range[i][1]] = bracket_range[i]
                    break
    bracket_range = sorted(bracket_range, key=lambda pair: pair[1] - pair[0])

    return bracket_range, bracket_map


def evaluate(expr):
    calculated_map = {}
    bracket_range, bracket_map = get_bracket_ranges(expr)

    def calc(lpos, rpos):
        result = None
        op: Optional[Callable] = None
        pos = lpos + 1
        while pos < rpos:
            literal = expr[pos]
            if literal.isdigit() or literal == "(":
                if literal == "(":
                    if pos not in calculated_map:
                        raise RuntimeError(
                            "Range {} not calculated yet".format(bracket_map[pos])
                        )
                    value = calculated_map[pos]
                    pos = bracket_map[pos][1] + 1
                else:
                    value = int(literal)
                    pos += 1

                if result is None:
                    result = value
                else:
                    if op is None:
                        raise RuntimeError("Op is undefined at pos: {}".format(pos))
                    result = op(result, value)
            elif literal == "+":
                op = operator.add
                pos += 1
            elif literal == "*":
                op = operator.mul
                pos += 1
            elif literal == ")":
                pos += 1
            else:
                raise RuntimeError("Unknown literal: {}".format(literal))

        calculated_map[lpos] = result

    for lpos, rpos in bracket_range:
        calc(lpos, rpos)

    return calculated_map[bracket_range[-1][0]]


def puzzle1():
    entries = ["(" + i + ")" for i in DATA.split("\n") if i]

    expressions = [
        entry.replace("(", "( ").replace(")", " )").split(" ") for entry in entries
    ]

    answer = sum(map(evaluate, expressions))

    print(answer)


def puzzle2():
    entries = ["(" + i + ")" for i in DATA.split("\n") if i]

    expressions = [
        entry.replace("(", "( ").replace(")", " )").split(" ") for entry in entries
    ]

    def do_find(expression, pos, direction):
        if direction == 1:
            r = range(pos, len(expression))
        elif direction == -1:
            r = range(pos, -1, -1)
        else:
            raise RuntimeError("Unable to setup find: direction={}".format(-1))

        balance = 0
        for i in r:
            if expression[i] == "(":
                balance += 1
            elif expression[i] == ")":
                balance -= 1
            if balance == 0:
                return i

    def find_left_end(expression, pos):
        return do_find(expression, pos, -1)

    def find_right_end(expression, pos):
        return do_find(expression, pos, 1)

    new_expressions = []
    # lets enclose every '+' expression within parentheses
    for expr in expressions:
        new_expression = list(expr)
        new_index = 0
        print(" ".join(expr))
        for index, literal in enumerate(expr):
            # debug
            line = list(" " * (len(new_expression) * 2))
            line[new_index * 2] = "^"
            # end debug
            if literal != "+":
                # debug
                print("".join(line))
                # end debug
                new_index += 1
                continue
            while new_expression[new_index] != literal:
                new_index += 1
            # debug
            line[new_index * 2] = "^"

            lpos = find_left_end(new_expression, new_index - 1)
            rpos = find_right_end(new_expression, new_index + 1)
            line[2 * lpos - 1] = "("
            line[2 * rpos + 1] = ")"
            # debug
            print("".join(line))
            # end debug

            if not (new_expression[lpos] == "(" and new_expression[rpos] == ")"):
                new_expression.insert(rpos + 1, ")")
                new_expression.insert(lpos, "(")

                if rpos == new_index + 1:
                    new_index += 3
                else:
                    new_index += 2
            else:
                new_index += 1
            # debug
            print(" ".join(new_expression))
            # end debug

        new_expressions.append(new_expression)

        print(" ".join(new_expression))

        answer = evaluate(new_expression)
        print("answer =", answer)
        print("")

    answer = sum(map(evaluate, new_expressions))
    print(answer)


if __name__ == "__main__":
    try:
        puzzle2()
    except NameError as e:
        if str(e) != "name 'puzzle2' is not defined":
            raise
        puzzle1()
