import operator
from functools import reduce
from pathlib import Path
from typing import List, Tuple, Union

DATA = (Path(__file__).parent / "data" / (Path(__file__).stem + ".txt")).read_text()

delim = ","


class Packet:
    def __init__(self, version: int, type_id: int, value: Union[int, List["Packet"]]) -> None:
        self.version = version
        self.type_id = type_id
        self.is_op = type_id != 4
        self.value = value

    def __repr__(self) -> str:
        return (
            f"<Packet "
            f"version={self.version} "
            f'type_id={f"operator({self.type_id})" if self.is_op else "literal"} '
            f'{f"packets=[{delim.join(map(repr, self.value))}]" if self.is_op else f"value={self.value}"}'
        )

    def get_sum_versions(self) -> int:
        result = self.version
        if self.is_op:
            result += sum(i.get_sum_versions() for i in self.value)
        return result

    def get_result(self) -> int:
        if self.type_id == 0:
            assert isinstance(self.value, list)
            assert all(map(lambda x: isinstance(x, Packet), self.value))
            result = sum(i.get_result() for i in self.value)
        elif self.type_id == 1:
            assert isinstance(self.value, list)
            assert all(map(lambda x: isinstance(x, Packet), self.value))
            result = reduce(operator.mul, map(Packet.get_result, self.value), 1)
        elif self.type_id == 2:
            assert isinstance(self.value, list)
            assert all(map(lambda x: isinstance(x, Packet), self.value))
            result = min(map(Packet.get_result, self.value))
        elif self.type_id == 3:
            assert isinstance(self.value, list)
            assert all(map(lambda x: isinstance(x, Packet), self.value))
            result = max(map(Packet.get_result, self.value))
        elif self.type_id == 4:
            assert isinstance(self.value, int)
            result = self.value
        elif self.type_id == 5:
            assert isinstance(self.value, list)
            assert all(map(lambda x: isinstance(x, Packet), self.value))
            assert len(self.value) == 2
            result = int(self.value[0].get_result() > self.value[1].get_result())
        elif self.type_id == 6:
            assert isinstance(self.value, list)
            assert all(map(lambda x: isinstance(x, Packet), self.value))
            assert len(self.value) == 2
            result = int(self.value[0].get_result() < self.value[1].get_result())
        elif self.type_id == 7:
            assert isinstance(self.value, list)
            assert all(map(lambda x: isinstance(x, Packet), self.value))
            assert len(self.value) == 2
            result = int(self.value[0].get_result() == self.value[1].get_result())
        else:
            assert False

        return result

    @classmethod
    def parse(cls, bits: str, offset: int = 0) -> Tuple[List["Packet"], int]:
        version = int(bits[offset : offset + 3], 2)
        type_id = int(bits[offset + 3 : offset + 6], 2)
        offset += 6
        if type_id == 4:
            value = 0
            while True:
                part = bits[offset : offset + 5]
                value = (value << 4) + int(part[1:], 2)
                offset += 5
                if part[0] == "0":
                    break
            result = value
        else:
            length_type = bits[offset]
            offset += 1
            sub_packets = []
            if length_type == "0":
                length_in_bits = int(bits[offset : offset + 15], 2)
                offset += 15
                end_of_subs = offset + length_in_bits
                while offset < end_of_subs:
                    packets, offset = cls.parse(bits, offset)
                    sub_packets.extend(packets)
            else:
                assert length_type == "1"
                length_in_packets = int(bits[offset : offset + 11], 2)
                offset += 11
                for _ in range(length_in_packets):
                    packets, offset = cls.parse(bits, offset)
                    sub_packets.extend(packets)

            result = sub_packets

        return [Packet(version, type_id, result)], offset


hex_map = {f"{i:X}": f"{i:04b}" for i in range(16)}


def puzzle1() -> None:
    record: str = DATA.strip()
    bits = "".join(hex_map[i] for i in record)
    packets, _ = Packet.parse(bits)
    print(f"Result: {packets[0].get_sum_versions()}")


def puzzle2() -> None:
    record: str = DATA.strip()
    bits = "".join(hex_map[i] for i in record)
    packets, _ = Packet.parse(bits)
    print(f"Result: {packets[0].get_result()}")


if __name__ == "__main__":
    try:
        puzzle2()
    except NameError as e:
        if str(e) != "name 'puzzle2' is not defined":
            raise
        puzzle1()
