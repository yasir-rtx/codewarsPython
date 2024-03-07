# Not very secure
# https://www.codewars.com/kata/526dbd6c8c0eb53254000110/train/python
from os import system
system("clear")


def alphanumeric(password):
    return password.isalnum()


print(alphanumeric("hello world_"))
print(alphanumeric("PassW0rd"))
print(alphanumeric("     "))
