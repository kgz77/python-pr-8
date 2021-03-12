# with open('test.txt', 'r', encoding='utf-8') as file:
#     f = file.readlines()
# print('Данные файла\n',f)
#
# s = []
#
# for i in range(len(f)):
#     s.append(f[i].split(','))
# print(s)
#
# kolNePar = 0
# kolPar = 0
#
# for i in range(len(s)):
#     if s[i][1] != '0':
#         kolPar += 1
#     if s[i][1] == '0':
#         kolNePar += 1
#
# print("\nКол-во парных : {}\nКол-во непарных : {}".format(kolPar,kolNePar))
# with open('test.txt', 'a',encoding='utf-8') as file2:
#     file2.write("\nКол-во парных : {}\nКол-во непарных : {}".format(kolPar,kolNePar))

# import csv
# file = csv.reader(open('test2.txt', 'r', encoding='utf-8'))
# s = []
#
# for row in file:
#     s.append(row)
#     print(row)
# print(s)
# kolNePar = 0
# kolPar = 0
#
# for i in range(len(s)):
#     if s[i][1] != '0':
#         kolPar += 1
#     if s[i][1] == '0':
#         kolNePar += 1
#
# print("\nКол-во парных : {}\nКол-во непарных : {}".format(kolPar,kolNePar))
# with open('test2.txt', 'a',encoding='utf-8') as file2:
#      file2.write("\nКол-во парных : {}\nКол-во непарных : {}".format(kolPar,kolNePar))

import json
with open('jsonTest', 'r', encoding='utf-8') as file:
    f = file.readlines()
print('Данные файла\n',f)

s = []

for i in range(len(f)):
    s.append(f[i].split(','))
print(s)

kolNePar = 0
kolPar = 0

for i in range(len(s)):
    if s[i][1] != '0':
        kolPar += 1
    if s[i][1] == '0':
        kolNePar += 1

print("\nКол-во парных : {}\nКол-во непарных : {}".format(kolPar,kolNePar))
with open('jsonTest', 'a',encoding='utf-8') as file2:
    file2.write("\nКол-во парных : {}\nКол-во непарных : {}".format(kolPar,kolNePar))

