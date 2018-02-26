# Module for assigning points and searching the distance between two points
class Point:
    """
    Class for assigning points and searching the distance between two points
    """
    def __init__(self, x=0, y=0):
        """
        (int, int) -> None
        Accepts two points
        """
        self.x = x
        self.y = y

    def distance(self, point):
        """
        (tuple) -> float
        Returns the distance between two points
        """
        return ((self.x - point.x)**2 + (self.y - point.y)**2) ** 0.5

    def __str__(self):
        """
        () -> str
        Returns information about points for comfortable reading for user
        """
        return "X:{} Y:{}".format(self.x, self.y)
