import hashlib

import sys

door_id = "ffykfhsq"


def puzzle1() -> None:
    index = 0
    password = ""

    md5 = hashlib.md5()
    for _ in range(len(door_id)):
        next_pass = None
        while next_pass is None:
            data = "{}{}".format(door_id, index)
            m = md5.copy()
            m.update(data.encode())
            result = m.hexdigest()
            if result[:5] == "00000":
                next_pass = result[5]
            index += 1
        password += next_pass
        sys.stdout.write("\r" + password)
    print("")


def puzzle2() -> None:
    index = 0
    password = [" "] * 8
    positions = [str(i) for i in range(8)]

    md5 = hashlib.md5()
    for _ in range(len(door_id)):
        while True:
            data = "{}{}".format(door_id, index)
            m = md5.copy()
            m.update(data.encode())
            result = m.hexdigest()
            if result[:5] == "00000":
                position = result[5]
                if position in positions:
                    position = int(position)
                    if password[position] == " ":
                        password[position] = result[6]
                        break
            index += 1
        sys.stdout.write("\r" + "".join(password))
    print("")
