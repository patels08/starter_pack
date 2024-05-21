
import math


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def distance(self, other_point: 'Point') -> int:
        return math.sqrt(((other_point.x-self.x) ** 2) +
                         ((other_point.y-self.y) ** 2))
