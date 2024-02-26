# Take a Ten Minutes Walk
# https://www.codewars.com/kata/54da539698b8a2ad76000228/python
from os import system
system("clear")


# def is_valid_walk(walk):
#     if walk.count('n') == walk.count('s') and walk.count('w') == walk.count('e'):
#         if len(walk) == 10:
#             return True
#     return False

def is_valid_walk(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('w') == walk.count('e')


print(is_valid_walk(['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's']))
print(is_valid_walk(['w', 'e', 'w', 'e', 'w',
      'e', 'w', 'e', 'w', 'e', 'w', 'e']))
print(is_valid_walk(['w']))
print(is_valid_walk(['n', 'n', 'n', 's', 'n', 's', 'n', 's', 'n', 's']))
