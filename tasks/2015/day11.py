class Password:
    _first_index = ord("a")
    _forbidden = [ord(char) - ord("a") for char in "iol"]
    _max_char = ord("z") - ord("a")

    def __init__(self, password):
        self._password = self._encode_password(password)

    def _condition1(self):
        for i in range(len(self._password) - 2):
            if (
                self._password[i] + 2
                == self._password[i + 1] + 1
                == self._password[i + 2]
            ):
                return True
        return False

    def _condition2(self):
        return not any(map(self._password.count, self._forbidden))

    def _condition3(self):
        i = 0
        pairs = 0
        while i < len(self._password) - 1 and pairs < 2:
            if self._password[i] == self._password[i + 1]:
                pairs += 1
                i += 1
            i += 1

        return pairs == 2

    def next_password(self):
        self._generate()
        while not (self._condition1() and self._condition2() and self._condition3()):
            self._generate()

        return self._decode_password(self._password)

    def _generate(self):
        memory = True
        for i in range(len(self._password) - 1, -1, -1):
            if memory:
                if self._password[i] == self._max_char:
                    self._password[i] = 0
                else:
                    self._password[i] += 1
                    memory = False

    @classmethod
    def _encode_password(cls, password):
        return [ord(char) - cls._first_index for char in password]

    @classmethod
    def _decode_password(cls, password):
        return "".join(chr(char + cls._first_index) for char in password)


def puzzle1():
    password = "hxbxwxba"

    password = Password(password)
    password.next_password()
    print(password.next_password())


def puzzle2():
    pass
