# This module gives you information about any classroom
class Classroom:
    """
    This class gives you common information about any room that you input
    """

    def __init__(self, number, capacity, equipment):
        """
        (str, int, list) -> None
        Accepts three arguments
        """
        self.number = number
        # Number of a room
        self.capacity = capacity
        # Capacity of a room
        self.equipment = equipment
        # All equipment of a room

    def is_larger(self, room):
        """
        tuple -> True or False
        Accepts room and compare length with self. Return True if self is
        larger of False if it is not
        """
        return True if self.capacity > room.capacity else False

    def equipment_differences(self, room):
        """
        tuple -> list
        Returns all equipment that is in self.equipment and
        not in room equipment
        """
        return [i for i in self.equipment if i not in room.equipment]

    def __str__(self):
        """
        () -> str
        Returns information about a room for comfortable reading for user
        """
        return "Classroom " + str(self.number) + " has a capacity of " + str(
            self.capacity) + " persons and has the " + "following equipment: "\
                           + str(", ".join(self.equipment))

    def __repr__(self):
        """
         () -> str
         Returns information about a room for comfortable reading for developer
        """
        return "Classroom({}, {}, {})".format(self.number, self.capacity,
                                              self.equipment)

