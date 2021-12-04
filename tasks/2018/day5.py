from main import data_path

DATA = data_path(__file__)


class Place:
    def __init__(self, value, enabled):
        self.value = value
        self.enabled = enabled

    def __repr__(self):
        return f"<{self.value}, {self.enabled}>"


class Node:
    def __init__(self, value):
        self.value = ord(value)
        self.next = None
        self.prev = None

    def __repr__(self):
        return f"<{chr(self.value)}>"


def puzzle1():
    with open(DATA, "r") as f:
        line = f.read()

    line = line.strip()

    head = Node(line[0])
    tail = head
    for i in line[1:]:
        tail.next = Node(i)
        prev = tail
        tail = tail.next
        tail.prev = prev

    cycles = 0
    while True:
        cycles += 1
        changes = 0

        i = head
        while i.next:
            if abs(i.value - i.next.value) == 32:
                if i.prev:
                    if i.next.next:
                        i.prev.next = i.next.next
                        i = i.prev
                        i.next.prev = i
                    else:
                        i.prev.next = None
                        i = i.prev
                else:
                    head = i.next.next
                    i = head
                    head.prev = None

                changes += 1
            else:
                i = i.next

        if not changes:
            break

    count = 0
    i = head
    result = []
    while True:
        if i:
            result.append(chr(i.value))
            count += 1
            i = i.next
        else:
            break

    print(count)


def puzzle2():
    with open(DATA, "r") as f:
        line = f.read()

    line = line.strip()

    shortest = None
    for j in range(ord("A"), ord("Z") + 1):
        skip = frozenset((j, j + 32))

        head = None
        tail = None
        for i in line:
            if ord(i) in skip:
                continue
            if head is None:
                head = Node(i)
                tail = head
            else:
                tail.next = Node(i)
                prev = tail
                tail = tail.next
                tail.prev = prev

        while True:
            changes = 0

            i = head
            while i.next:
                if abs(i.value - i.next.value) == 32:
                    if i.prev:
                        if i.next.next:
                            i.prev.next = i.next.next
                            i = i.prev
                            i.next.prev = i
                        else:
                            i.prev.next = None
                            i = i.prev
                    else:
                        head = i.next.next
                        i = head
                        head.prev = None

                    changes += 1
                else:
                    i = i.next

            if not changes:
                break

        count = 0
        i = head
        result = []
        while True:
            if i:
                result.append(chr(i.value))
                count += 1
                i = i.next
            else:
                break

        if shortest:
            shortest = min(shortest, count)
        else:
            shortest = count

    print(shortest)
