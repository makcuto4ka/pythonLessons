try:
    a = int(input("Введите первое целое число \n"))
    b = int(input("Введите второе целое число \n"))
    c = int(input("Введите третье целое число \n"))
    if a<b:
        if a<c:
            y=a
        else:
            y=c
    else:
        if b<c:
            y=b
        else:
            y=c
    print("Минимальное число ", y)
except ValueError:
  print("Ошибка, вводи целые!")