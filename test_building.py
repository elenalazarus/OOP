from building import AcademicBuilding
from classroom import Classroom

classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
classroom_007 = Classroom('007', 12, ['TV'])
classroom_008 = Classroom('008', 25, ['PC', 'projector'])
classrooms = [classroom_016, classroom_007, classroom_008]
building = AcademicBuilding('Kozelnytska st. 2a', classrooms)

# Classroom 016 has a capacity of 80 persons and has the following equipment:
# PC, projector, mic
# Classroom 007 has a capacity of 12 persons and has the following equipment:
# TV
# Classroom 008 has a capacity of 25 persons and has the following equipment:
# PC, projector
for room in building.classrooms:
    print(room)

# [('projector', 2), ('PC', 2), ('mic', 1), ('TV', 1)]
print(building.total_equipment())

# Kozelnytska st. 2a
# Classroom 016 has a capacity of 80 persons and has the following equipment:
# PC, projector, mic
# Classroom 007 has a capacity of 12 persons and has the following equipment:
# TV
# Classroom 008 has a capacity of 25 persons and has the following equipment:
# PC, projector
print(building.__str__())
