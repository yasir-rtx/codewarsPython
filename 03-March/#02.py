# Multiples of 3 or 5
# https://www.codewars.com/kata/514b92a657cdc65150000006/train/python
from os import system
system("cls")


# def solution(number):
#     result = []
#     for i in range(number):
#         if i == 0:
#             continue
#         elif i % 3 == 0:
#             result.append(i)
#         elif i % 5 == 0:
#             result.append(i)
#     return sum(result)

def solution(number):
    return sum([i for i in range(1, number) if i % 3 == 0 or i % 5 == 0])


print((solution(4)))
print((solution(6)))
print((solution(16)))
print((solution(3)))
print((solution(5)))
print((solution(15)))
print((solution(0)))
print((solution(-1)))
print((solution(10)))
print((solution(20)))
print((solution(200)))
