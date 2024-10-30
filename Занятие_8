#1
print('\n#1')

import re
s=input("Введите строку: ")
while s!='':
    if re.fullmatch(r'[А-Я]\d{3}[А-Я]{2}\d{2,3}', s):
        print('Это регистрационный номер частного автомобиля.')
    elif re.fullmatch(r'[А-Я]{2}\d{4,5}', s):
        print('Это регистрационный номер такси.')
    else:
        print('Строка не является регистрационным номером.')
    s=input("Введите строку: ")

#2
print('\n#2')

import re
from functools import reduce
file = open('Занятие_8_Текст.txt', 'r', encoding='utf-8')
s = file.readlines()
words= reduce(lambda x,y:  x[:-1]+' '+y, s).split()
print(words)
print(list(filter(lambda x: re.fullmatch(r'\b[А-Яа-яёЁ]+[-]?[А-Яа-яёЁ]+\b',x) or re.fullmatch(r'\b[A-Za-z]+[-]?[A-Za-z]+\b',x), words)))

#3
print('\n#3')

import re
from functools import reduce
s='Уважаемые! Если вы к 09:00 не вернёте чемодан, то уже в 09:00:01 я за себя не отвечаю.'
s=s.split()
x=list(filter(lambda x: re.search(r'\b(0[0-9]|1[0-9]|2[0-4])[:](0[0-9]|[0-9]{2})\b',x) ,s))
s= reduce(lambda x,y:  x+' '+y, s)
for i in x:
    s=s.replace(i,'(TBD)',1)
print(s)

#4
print('\n#4')

import re
s='Владимир устроился на работу в одно очень важное место. И в первом же документе он ничего не понял, там были сплошные ФГУП НИЦ ГИДГЕО, ФГОУ ЧШУ АПК и т.п. '
x=re.findall(r'\b[А-ЯЁ][А-ЯЁ ]*[А-ЯЁ]\b',s)
print(x)