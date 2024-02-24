# Who likes it?
# https://www.codewars.com/kata/5266876b8f4bf2da9b000362/python
from os import system

system("clear")


# def likes(names):
#     list_nama = ""
#     for i, name in enumerate(names):
#         if (i + 1 != len(names)):
#             list_nama += name + " and "
#         else:
#             list_nama += name
#     return list_nama + " like this"

# def likes(names):
#     text = ""
#     if (len(names) == 0):
#         text = "no one likes this"
#     elif (len(names) == 1) :
#         text = names[0] + " likes this"
#     elif (len(names) == 2) :
#         text = names[0] + " and " + names[1] + " like this"
#     elif (len(names) == 3) :
#         text = names[0] + ", " + names[1] + " and " + names[2] + " like this"
#     else :
#         text = names[0] + ", " + names[1] + " and " + str(len(names)-2) +  " others" + " like this"
#     return text


def likes(names):
    n = len(names)
    return {
        0: "no one likes this",
        1: "{} likes this",
        2: "{} and {} like this",
        3: "{}, {} and {} like this",
        4: "{}, {} and {others} others like this",
    }[min(4, n)].format(*names[:3], others=n - 2)


print(likes([]))
print(likes(["Peter"]))
print(likes(["Jacob", "Alex"]))
print(likes(["Max", "John", "Mark"]))
print(likes(["Alex", "Jacob", "Mark", "Max"]))
