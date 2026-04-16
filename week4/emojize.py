from emoji import emojize

str = input("Input : ")
str = str.strip()

print(emojize(str, language='alias'))

