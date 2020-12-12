from __future__ import annotations


class Point:
    directions = {0: (1, 0),
                  90: (0, 1),
                  180: (-1, 0),
                  270: (0, -1)}

    def __init__(self: Point, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __add__(self: Point, other: Point) -> Point:
        return Point(self.x + other.x, self.y + other.y)

    def __iadd__(self: Point, other: Point) -> Point:
        self.x += other.x
        self.y += other.y
        return self

    def go_in_direction(self: Point, direction: int, mag: int):
        self.x += self.directions[direction][0] * mag
        self.y += self.directions[direction][1] * mag

    def manhatten_distance_origin(self: Point) -> int:
        return abs(self.x) + abs(self.y)

    def add_x(self: Point, x: int):
        self.x += x

    def add_y(self: Point, y: int):
        self.y += y

    def rotate(self: Point, by: int):
        by = by % 360
        tmp: int
        if by == 90:
            tmp = self.x
            self.x = - self.y
            self.y = tmp
        elif by == 180:
            self.x = -self.x
            self.y = -self.y
        elif by == 270:
            tmp = self.x
            self.x = self.y
            self.y = -tmp

    def move_to_waypoint(self: Point, waypoint: Point, mag: int):
        self.x += waypoint.x * mag
        self.y += waypoint.y * mag

    def __str__(self):
        return f"({self.x}, {self.y})"
