a = float(input("Введите число \n"))
s=0
k=0
while a!=0:
    s+=a
    k+=1
    a = float(input("Введите число \n"))
print('Сумма чисел последовательности:',s) 
print('Количество чисел последовательности:',k)