from rect.point import Point
from rect.rectangle import Rectangle

if __name__=="__main__":
    x1 = Point(1,1)
    x2 = Point(2,2)
    r = Rectangle(x1, x2)
    print(x1.distance(x2))
    print(r.get_diagonal())