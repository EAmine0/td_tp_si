# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import csv
import character

character_list = []

with open('characters.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar=' ')
    next(reader)
    for row in reader:
        print(' , '.join(row))
    word = [row[0].split(",")[0] for row in reader]


print(character_list)
p1 = character.Character("test", "", 2, "", 2)
print(p1.age)