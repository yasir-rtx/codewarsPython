# Disemvowel Trolls
# https://www.codewars.com/kata/52fba66badcd10859f00097e

def disemvowel(string_):
    return "".join(word for word in string_ if word not in 'aiueoAIUEO')

print(disemvowel("This website is for losers LOL!"))
