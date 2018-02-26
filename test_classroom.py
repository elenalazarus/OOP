from classroom import Classroom

room1 = Classroom('016', 80, ['PC', 'projector', 'mic'])
room2 = Classroom('007', 12, ['TV'])

# ['PC', 'projector', 'mic']
print(room1.equipment_differences(room2))

# Classroom(016, 80, ['PC', 'projector', 'mic'])
print(room1.__repr__())

# Classroom(007, 12, ['TV'])
print(room2.__repr__())

# False
print(room2.is_larger(room1))

# True
print(room1.is_larger(room2))

# ['PC', 'projector', 'mic']
print(room1.equipment_differences(room2))

# ['TV']
print(room2.equipment_differences(room1))

# Classroom 016 has a capacity of 80 persons and has the following
# equipment: PC, projector, mic
print(room1.__str__())

# Classroom 007 has a capacity of 12 persons and has the following
# equipment: TV
print(room2.__str__())
