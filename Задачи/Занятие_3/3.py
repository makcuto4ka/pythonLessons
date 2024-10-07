m=[1, '2', 3, 4, '5', '!', 'FF', '5', '7!']
s=0
for i in m:
  si=str(i)
  for j in si:
    if j in '1234567890':
      s+= int(j)
print('Сумма элементов списка:', s)
