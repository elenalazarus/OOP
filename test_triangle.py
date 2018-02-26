from triangle import Triangle
from point import Point

triangle = Triangle(Point(1, 1), Point(3, 1), Point(2, 3))

# True
print(triangle.is_triangle())

# 6.47213595499958
print(triangle.perimeter())

# 2.0
print(triangle.area())