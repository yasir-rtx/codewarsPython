# Categorize New Member
# https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa/python


# def open_or_senior(data):
#     categories = []
#     for x, y in data: categories.append("Senior") if (x >= 55 and y > 7) else categories.append("Open")
#     return categories\

def open_or_senior(data):
    return ["Senior" if (x >= 55 and y > 7) else "Open" for x, y in data]

# print(open_or_senior([(45, 12),(55,21),(19, -2),(104, 20)]))
print(open_or_senior([(45, 12), (55, 21), (19, -2), (104, 20)]))
print(open_or_senior([(16, 23),(73,1),(56, 20),(1, -1)]))
