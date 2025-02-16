# # 1.1
# import numpy as np

# numbers = [2, -93, -2, 8, None, -44, -1, -85, -14,
#            90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# # TODO заменить значение пропущенного элемента средним арифметическим

# k = len(numbers)
# sm = numbers.remove(None)
# print(sum(numbers)/k)
# print("Измененный список:", numbers)

# # 2.1
# money_capital = 20000  # Подушка безопасности
# salary = 5000  # Ежемесячная зарплата
# spend = 6000  # Траты за первый месяц
# increase = 0.05  # Ежемесячный рост цен

# # TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
# k = 0
# while money_capital >= 0:
#     money_capital += salary
#     money_capital -= spend + spend*increase*k
#     k += 1
# print("Количество месяцев, которое можно протянуть без долгов:", k-1)

# # 3.3
# from matplotlib import pyplot as plt
# import os

# dir = os.getcwd()
# x = np.linspace(0, 2*np.pi, 1000)

# plt.rcParams["figure.figsize"] = [5, 5]
# plt.rcParams["figure.autolayout"] = True


# def sin(x):
#     y = [np.sin(i) for i in x]
#     return y


# def cos(x):
#     y = [np.cos(i) for i in x]
#     return y


# plt.grid()
# plt.arrow(0, 0, 2*np.pi+0.5, 0, width=0.01)
# plt.arrow(0, -1, 0, 2, width=0.05)
# y0=[0,np.pi/2, np.pi, np.pi*2]
# for i in y0:
#     plt.scatter(i, 0)
#     plt.annotate( f'({round(i,2)},0)', (i-0.05, 0.05)) 
# plt.plot(x, sin(x), label='sin(x)', color='red')
# plt.plot(x, cos(x), label='cos(x)', color='blue')
# plt.xlabel('Ось X')
# plt.ylabel('Ось Y')
# plt.legend()
# plt.show()


for i in range(1000):
    print(f'{'0'*(3-len(str(i)))+str(i)}')