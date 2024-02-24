# Printer Errors
# https://www.codewars.com/kata/56541980fa08ab47a0000040/python
from os import system
system("clear")

# def printer_error(s):
#     count = 0
#     for i in s:
#         if i in 'nopqrstuvwxyz' : count+=1
#     return f"{count}/{len(s)}"

def printer_error(s):
    return "{}/{}".format(len([x for x in s if x in 'nopqrstuvwxyz']), len(s))

print(printer_error("aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"))
print(printer_error("kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"))
print(printer_error("kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyzuuuuu"))