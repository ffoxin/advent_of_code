from operator import itemgetter


class Room:
    _initialized = False

    @classmethod
    def static_initialization(cls):
        if not cls._initialized:
            cls._first_char, cls._last_char = ord("a"), ord("z")
            cls._alphabet = [
                chr(i + cls._first_char)
                for i in range(cls._last_char - cls._first_char + 1)
            ]
            cls._mod = len(cls._alphabet)
            cls._initialized = True

    def __init__(self, line):
        self.static_initialization()

        self._enc_name, room_suffix = line.rsplit("-", 1)
        room_id, self._checksum = room_suffix[:-1].split("[")
        self.room_id = int(room_id)

    def is_valid(self):
        return self._checksum == self._get_checksum()

    def _get_checksum(self):
        stats = {}
        for char in self._enc_name:
            if char == "-":
                continue
            if char in stats:
                stats[char] += 1
            else:
                stats[char] = 1
        sorted_names = sorted(stats.items(), key=itemgetter(0))
        sorted_values = sorted(sorted_names, key=itemgetter(1), reverse=True)
        return "".join([pair[0] for pair in sorted_values[:5]])

    def decrypt(self):
        new_name = ""
        for char in self._enc_name:
            if char != "-":
                char = chr(
                    (ord(char) - self._first_char + self.room_id) % self._mod
                    + self._first_char
                )
            new_name += char
        return new_name


def puzzle1():
    data = "tasks/data/day4.txt"

    room_sum = 0
    with open(data, "r") as f:
        for line in f.readlines():
            room = Room(line[:-1])
            if room.is_valid():
                room_sum += room.room_id

    print(room_sum)


def puzzle2():
    data = "tasks/data/day4.txt"

    with open(data, "r") as f:
        for line in f.readlines():
            room = Room(line[:-1])
            if room.is_valid():
                true_name = room.decrypt()
                if all(
                    [
                        check in true_name
                        for check in ["north", "pole", "object", "storage"]
                    ]
                ):
                    print("{}: {}".format(true_name, room.room_id))
