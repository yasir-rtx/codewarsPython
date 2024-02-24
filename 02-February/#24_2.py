# Sum of two lowest positive integers
# https://www.codewars.com/kata/558fc85d8fd1938afb000014/python
from os import system

system("clear")

# def sum_two_smallest_numbers(numbers):
#     numbers.sort()
#     x,y = numbers[:2]
#     return x+y


def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])


print(sum_two_smallest_numbers([5, 8, 12, 18, 22]))
print(sum_two_smallest_numbers([7, 15, 12, 18, 22]))
print(sum_two_smallest_numbers([25, 42, 12, 18, 22]))
