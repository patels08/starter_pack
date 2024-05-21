from rect.point import Point


class Rectangle:
    def __init__(self, first_point: Point, second_point: Point):
        self.valid_rectangle(first_point, second_point)
        self._set_lower_upper_points(first_point, second_point)

    @staticmethod
    def valid_rectangle(first_point: Point, second_point: Point):
        if first_point.x == second_point.x or first_point.y == second_point.y:
            raise Exception('Rectangle coordinates are invalid.'
                            'Cannot build rectangle')

    def _set_lower_upper_points(self, first_point: Point, second_point: Point):
        if first_point.x > second_point.x:
            lower_x = second_point.x
            second_point.x = first_point.x
            first_point.x = lower_x

        if first_point.y > second_point.y:
            lower_y = second_point.y
            second_point.y = first_point.y
            first_point.y = lower_y

        self.lower_left = first_point
        self.upper_right = second_point

    def point_inside_rectangle(self, third_point):
        if self.lower_left.x < third_point.x < self.upper_right.x\
           and self.lower_left.y < third_point.y < self.upper_right.y:
            return True

        return False

    def get_diagonal(self):
        return self.lower_left.distance(self.upper_right)
