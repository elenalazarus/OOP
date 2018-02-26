from point import Point


class Triangle:
    """
    This class gelp you to get to know a possibility of existing your
    triangle, perimeter of a triangle and its area
    """

    def __init__(self, x, y, z):
        """
        (tuple, tuple, tuple) -> None
        Accepts three points
        """
        self.x = x
        self.y = y
        self.z = z

    def is_triangle(self):
        """
        () -> True or False
        Return True if such triangle exists else False
        """
        # Sides of a triangle
        line1 = Point.distance(self.x, self.y)
        line2 = Point.distance(self.y, self.z)
        line3 = Point.distance(self.x, self.z)
        # Check if such exists
        if line1 + line2 <= line3 or line2 + line3 <= line1 or line1 \
                + line3 <= line2:
            return False
        return True

    def perimeter(self):
        """
        () -> float
        Return perimeter of a triangle
        """
        # If such triangle doesn't exist
        if not self.is_triangle():
            return "Sorry, this triangle doesn't exist"
        # Sides of a triangle
        line1 = Point.distance(self.x, self.y)
        line2 = Point.distance(self.y, self.z)
        line3 = Point.distance(self.x, self.z)
        return line1 + line2 + line3

    def area(self):
        """
        () -> float
        Return area of a triangle
        """
        # If such triangle doesn't exist
        if not self.is_triangle():
            return "Sorry, this triangle doesn't exist"
        # Sides of a triangle
        a = Point.distance(self.x, self.y)
        b = Point.distance(self.y, self.z)
        c = Point.distance(self.x, self.z)
        # Half of perimeter
        p = self.perimeter() / 2
        # Heron's formula
        s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        return s
