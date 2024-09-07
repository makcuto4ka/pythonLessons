a = float(input("Введите первое число \n"))
b = float(input("Введите второе число \n"))
try:
  print(a/b)
except ZeroDivisionError:
  print("Деление на 0!")