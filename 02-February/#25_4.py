# Is this a triangle?
# https://www.codewars.com/kata/56606694ec01347ce800001b/python
from os import system
system("clear")


# def is_triangle(a, b, c):
#     sides = a, b, c
#     a, b, c = sorted(sides)
#     if (a+b > c):
#         return True
#     else:
#         return False

def is_triangle(a, b, c):
    a, b, c = sorted([a, b, c])
    return True if a+b > c else False

# def is_triangle(a, b, c):
#     return (a < b+c) and (b < a+c) and (c < a+b)


print(is_triangle(1, 2, 2))
print(is_triangle(7, 2, 2))
# print(is_triangle(1, 2, 3))
# print(is_triangle(-1, 3, 2))
# print(is_triangle(3, 1, 2))
# print(is_triangle(5, 1, 2))
# print(is_triangle(1, 2, 5))
# print(is_triangle(2, 5, 1))
