s = input('Введите строку: \n')
s=s.split()
k=0
for i in s:
    if i[0]=='е':
        k+=1
print('Количество слов, начинающихся с буквы "е":', k)