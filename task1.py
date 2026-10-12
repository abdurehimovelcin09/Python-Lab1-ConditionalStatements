set1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]
set2 = [2, 3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23, 26, 27, 30, 31]
set3 = [4, 5, 6, 7, 12, 13, 14, 15, 20, 21, 22, 23, 28, 29, 30, 31]
set4 = [8, 9, 10, 11, 12, 13, 14, 15, 24, 25, 26, 27, 28, 29, 30, 31]
set5 = [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
birthday = 0
a = int(input("Is your birthday included in this set1: 1 for Yes, 0 for No"))
if a == 1:
    birthday = birthday + 1
a = int(input("Is your birthday included in this set2: 1 for Yes, 0 for No"))
if a == 1:
    birthday = birthday + 2
a = int(input("Is your birthday included in this set3: 1 for Yes, 0 for No"))
if a == 1:
    birthday = birthday + 4
a = int(input("Is your birthday included in this set4: 1 for Yes, 0 for No"))
if a == 1:
    birthday = birthday + 8
a = int(input("Is your birthday included in this set5: 1 for Yes, 0 for No"))
if a == 1:
    birthday = birthday + 16
print("Your birthday is:", birthday)
