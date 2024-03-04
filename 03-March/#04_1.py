# Directions Reduction
# https://www.codewars.com/kata/550f22f4d758534c1100025a/train/python
from os import system
system("clear")


def dir_reduc(path):
    opposite = [['NORTH', 'SOUTH'], ['SOUTH', 'NORTH'],
                ['WEST', 'EAST'], ['EAST', 'WEST']]
    for i in range(len(path)-1):
        if path[i:i+2] in opposite:
            del [path[i:i+2]]
            return dir_reduc(path)
    return path


# print(dir_reduc(["NORTH", "SOUTH", "SOUTH", "EAST",
#       "WEST", "NORTH", "WEST"]), "Should be WEST")
# print((dir_reduc([])))
# print((dir_reduc(["NORTH", "WEST", "SOUTH", "EAST"])))
# print(
#     (dir_reduc(["NORTH", "SOUTH", "EAST", "WEST", "NORTH", "NORTH", "SOUTH", "NORTH", "WEST", "EAST"])))
print((dir_reduc(['NORTH', 'NORTH', 'EAST', 'SOUTH',
      'EAST', 'EAST', 'SOUTH', 'SOUTH', 'SOUTH', 'NORTH'])))
