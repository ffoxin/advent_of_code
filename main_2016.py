from importlib import import_module


from datetime import datetime, tzinfo, timedelta


def main():
    class FixedOffset(tzinfo):
        """Fixed offset in minutes east from UTC."""
        ZERO = timedelta(0)
        HOUR = timedelta(hours=1)

        def __init__(self, offset, name):
            self.__offset = timedelta(minutes=offset)
            self.__name = name

        def utcoffset(self, dt):
            return self.__offset

        def tzname(self, dt):
            return self.__name

        def dst(self, dt):
            return self.ZERO

    aoc_now = datetime.now(tz=FixedOffset(-5 * 60, 'AoC'))
    puzzle_module = 'tasks.day{}'.format(aoc_now.day)
    module = import_module(puzzle_module)

    module.puzzle1()
    module.puzzle2()


if __name__ == '__main__':
    main()
