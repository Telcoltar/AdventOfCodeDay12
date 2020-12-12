import logging

logger = logging.getLogger(__name__)


def get_input_data(input_file_name: str) -> list[tuple[str, int]]:
    f = open(input_file_name, "r")
    lines: list[tuple[str, int]] = []
    command: str
    magnitude: int
    for line in f:
        command = line.strip()[0]
        magnitude = int(line.strip()[1:])
        lines.append((command, magnitude))
    f.close()
    return lines
