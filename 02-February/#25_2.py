# Friend or Foe?
# https://www.codewars.com/kata/55b42574ff091733d900002f
from os import system
system("clear")


def friend(names):
    return [name for name in names if len(name) == 4]


print(friend(["Ryan", "Kieran", "Mark",]))