'''   На занятие '''
print('На занятие')

#1
print('\n#1')

s = input('Введите строку: ')
s=s.split()
k=0
f=''
for i in s:
    if i[0]=='е':
        k+=1
        f+=i+' '
print('Количество слов, начинающихся с буквы "е":', k)
print(f)

#2
print('\n#2')

s = input('Введите строку: ')
k=s.count(':')
s=s.replace(':', '%')
print('Получившиеся строка:',s) 
print('Количество замен:',k)

#3
print('\n#3')

s = input('Введите строку: ')
k=s.count('.')
s=s.replace('.', '')
print('Получившиеся строка:',s) 
print('Количество удаленных символов:',k)


#4
print('\n#4')

from random import randint
m=[randint(-100, 100) for x in range(10)]
print(m)
for i in range(0,len(m)-1):
    if m[i]<0 and m[i+1]<0:
        print('Пара отрицательных чисел:',m[i],m[i+1])



#5
print('\n#5')

try:
  n = int(input('N: '))
  m=[int(input()) for i in range(n)]
  sortm=sorted(m)
  print('Индекс минимального элемента:', m.index(sortm[0]))
except ValueError:
  print("Ошибка, вводи целые!")

#6
print('\n#6')

from random import randint
m=[randint(1, 20) for x in range(8)]
for i in range(len(s)):
    if m[i]<15:
        m[i]*=2
print('Преобразованный массив:', m)


'''   Домашняя работа '''
print('\nДомашняя работа')

#1
print('\n#1')

s = input('Введите строку: ')
k=m=0
for i in range(len(s)):
    if s[i]=='н':
        k+=1
    else:
        m=max(m,k)
        k=0
s=s.replace('н','!')
print('Максимальное количество подряд идущих букв «н»:', m)
print('Преобразованная строка:', s)

#2
print('\n#2')

s = input('Введите строку: ')
for i in '[{':
  s=s.replace(i,'(')
for i in '}]':
  s=s.replace(i,')')
for i in range(len(s)):
    if s[i]=='(':
        a=i
    elif s[i]==')':
        b=i
print(s[a+1:b])


#3
print('\n#3')

s = input('Введите строку: ')
s=s.split()
a=''
for i in s:
    if i[0].lower()=='а'and i[-1]=='я':
        a+= i + ' '
print(a)