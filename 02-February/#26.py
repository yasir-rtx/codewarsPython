# Count characters in your string
# https://www.codewars.com/kata/52efefcbcdf57161d4000091/train/python
from os import system
system("clear")


# def count(s):
#     if s != '':
#         x = {}
#         for y in s:
#             for word in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
#                 result = s.count(word)
#                 if result != 0:
#                     x.update({word: result})
#             return x
#     else:
#         return {}

def count(s):
    return {word: s.count(s) for word in s}


print(count('aba'))
print(count(''))
print(count('QWFALVQoSWOMQh'))
