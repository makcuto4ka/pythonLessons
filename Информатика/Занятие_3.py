'''   На занятие '''
print('На занятие')

#1
print('\n#1')

a = float(input("Цена 1 кг конфет \n"))
for i in range(1,11):
    print('Стоимость', i,'кг конфет равна', i*a)

#2
print('\n#2')

a = float(input("Введите число \n"))
s=0
k=0
while a!=0:
    s+=a
    k+=1
    a = float(input("Введите число \n"))
print('Сумма чисел последовательности:',s) 
print('Количество чисел последовательности:',k)

#3
print('\n#3')

m=[1, '2', 3, 4, '5', '!', 'FF', '5', '7!']
s=0
for i in m:
  si=str(i)
  for j in si:
    if j in '1234567890':
      s+= int(j)
print('Сумма элементов списка:', s)


'''   Домашняя работа '''
print('\nДомашняя работа')

#1
print('\n#1')

n = int(input("Введите число n\n"))
if n>100:
    print('Вы превысили верхний предел!')
else:
  s=0
  for i in range(1,n+1):
      s+=i**3
print('Сумма кубов натуральных чисел от 1 до',n,'равна',s)

#2
print('\n#2')

m=''
for i in range(1,11):
    for j in range(1,11):
      m+=str(j*i)+' '*(3-len(str(j*i)))
    print(m)
    m=''

def f(n):
  for i in range(2,int(n**0.5)+1):
    if n%i==0:
      return 0
      break
  return 1
st = int(input("От "))
fn = int(input("До "))
for i in range(st,fn+1):
  if f(i)==1:
    print(i)
