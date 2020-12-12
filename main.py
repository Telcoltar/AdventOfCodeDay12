import argparse
from commenUtils import get_input_data
import logging
from Point import Point

parser = argparse.ArgumentParser()
parser.add_argument("--log", default="info")

options = parser.parse_args()

level = logging.INFO

if options.log.lower() == "debug":
    level = logging.DEBUG

logging.basicConfig(format='%(asctime)s | %(name)s | %(levelname)s | %(message)s',
                    level=level)

logger = logging.getLogger(__name__)


def solution_part_1(file_name: str) -> int:
    commands: list[tuple[str, int]] = get_input_data(file_name)
    current_direction: int = 0
    current_position: Point = Point(0, 0)
    for commmand, mag in commands:
        if commmand == "N":
            current_position.add_y(mag)
        elif commmand == "S":
            current_position.add_y(-mag)
        elif commmand == "E":
            current_position.add_x(mag)
        elif commmand == "W":
            current_position.add_x(-mag)
        elif commmand == "R":
            current_direction = (current_direction - mag) % 360
        elif commmand == "L":
            current_direction = (current_direction + mag) % 360
        elif commmand == "F":
            current_position.go_in_direction(current_direction, mag)
        logger.debug(f"Command: {commmand}, magnitude: {mag}, current position {current_position}")
    return current_position.manhatten_distance_origin()


def solution_part_2(file_name: str) -> int:
    commands: list[tuple[str, int]] = get_input_data(file_name)
    waypoint: Point = Point(10, 1)
    current_position: Point = Point(0, 0)
    for commmand, mag in commands:
        if commmand == "N":
            waypoint.add_y(mag)
        elif commmand == "S":
            waypoint.add_y(-mag)
        elif commmand == "E":
            waypoint.add_x(mag)
        elif commmand == "W":
            waypoint.add_x(-mag)
        elif commmand == "R":
            waypoint.rotate(-mag)
        elif commmand == "L":
            waypoint.rotate(mag)
        elif commmand == "F":
            current_position.move_to_waypoint(waypoint, mag)
        logger.debug(f"Command: {commmand}, magnitude: {mag},"
                     f"current position {current_position}, waypoint: {waypoint}")
    return current_position.manhatten_distance_origin()


if __name__ == '__main__':
    logger.info(solution_part_1("inputData.txt"))
    logger.info(solution_part_2("inputData.txt"))
