# Beginner Series #3 Sum of Numbers
# https://www.codewars.com/kata/55f2b110f61eb01779000053/python
from os import system
system("clear")


# def get_sum(a, b):
#     sumNum = []
#     if a > b:
#         a, b = b, a
#     for i in range(a, b + 1):
#         sumNum.append(i)
#     return sum(sumNum)

# def get_sum(a, b):
#     if a > b:
#         a, b = b, a
#     return sum([i for i in range(a, b + 1)])

def get_sum(a, b):
    return sum(range(min(a, b), max(a, b)+1))


print(get_sum(0, 1))
print(get_sum(0, -1))
print(get_sum(3, 1))
print(get_sum(-3228, -3271))
