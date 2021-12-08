import os


def data_path(day_py):
    day_path, day = os.path.split(day_py)
    return os.path.join(day_path, "data", day.replace(".py", ".txt"))
