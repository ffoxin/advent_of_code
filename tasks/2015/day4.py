import hashlib


def puzzle1():
    secret = "iwrupvqb"
    index = 1
    md5 = hashlib.md5()
    while True:
        key = "{}{}".format(secret, index)
        hasher = md5.copy()
        hasher.update(key.encode())
        if hasher.hexdigest().startswith("00000"):
            print(index)
            return
        index += 1


def puzzle2():
    secret = "iwrupvqb"
    index = 1
    md5 = hashlib.md5()
    while True:
        key = "{}{}".format(secret, index)
        hasher = md5.copy()
        hasher.update(key.encode())
        if hasher.hexdigest().startswith("000000"):
            print(index)
            return
        index += 1
