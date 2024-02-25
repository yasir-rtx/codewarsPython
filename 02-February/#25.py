# Duplicate Encoder
# https://www.codewars.com/kata/54b42f9314d9229fd6000d9c

from os import system
system("clear")


def duplicate_encode(word):
    return "".join(["(" if word.lower().count(x) == 1 else ")" for x in word.lower()])


# print((duplicate_encode("")))
print((duplicate_encode("din"), "((("))
print((duplicate_encode("recede"), "()()()"))
print((duplicate_encode("Success"), ")())())", "should ignore case"))
print((duplicate_encode("(( @"), "))(("))
