# Tribonacci Sequence
# https://www.codewars.com/kata/556deca17c58da83c00002db/python
from os import system
system("clear")


# def tribonacci(signature, n):
#     sequence = []
#     if n == 0:
#         return sequence
#     else:
#         for i in range(n):
#             sequence.append(signature[i]) if (i < 3) else sequence.append(sequence[i-3] + sequence[i-2] + sequence[i-1])
#         return sequence

def tribonacci(signature, n):
    seq = signature[:n]
    for i in range(n-3) : seq.append(sum(seq[-3:]))
    return seq


print(tribonacci([4, 5, 6], 10))
print(tribonacci([1, 1, 1], 0))
