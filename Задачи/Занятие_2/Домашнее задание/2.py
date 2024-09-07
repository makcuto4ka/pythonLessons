s = float(input("Введите сумму покупки \n"))
if s>20:
    fs=s*0.65
else:
    fs=s
print('Итоговая сумма покупки',round(fs,2))
print('Размер предоставленной скидки',round(s-fs,2))