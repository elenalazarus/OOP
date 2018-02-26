# This module gives you information about all classrooms
# in the academic building
from classroom import Classroom


class AcademicBuilding:
    """
    This class gives you common information about classrooms
    in the academic building
    """

    def __init__(self, adress, classrooms):
        """
        (str, list) -> None
        Accepts two arguments
        """
        self.adress = adress
        self.classrooms = classrooms

    def total_equipment(self):
        """
        () -> list
        Returns list with all equipment from all rooms with its number
        """
        all_equipment = []
        right_equipment = []
        for room in self.classrooms:
            for e in room.equipment:
                # Add all equipment from every room
                all_equipment.append(e)
        # Sort information for comfortable reading
        for e in all_equipment:
            right_equipment.append((e, all_equipment.count(e)))
        return list(set(right_equipment))

    def __str__(self):
        """
        () -> str
        Returns information about all rooms and adress for comfortable
        reading for user
        """
        return self.adress + '\n' + "\n".join(
            str(i) for i in self.classrooms)

