# # class ClassA(object):
# #     def __init__(self, var1=5, var2=6):
# #         ClassA.var1 = var1
# #         ClassA.var2 = var2

# #     def methodA(self):
# #         ClassA.var1 = ClassA.var1 + ClassA.var2
# #         return ClassA.var1



# # class ClassB(ClassA):
# #     def __init__(self):
# #         print( ClassA.var1)
# #         print (ClassA.var2)

# # object1 = ClassA()
# # sum = object1.methodA()
# # object2 = ClassB()
# # a= {key:value for (key,value) in [['1','2'],['4','5']]}
# # print(a)
# Создаем независимые списки и словари для каждой ячейки
a = [[{1: 2} for _ in range(3)] for _ in range(3)]
a[0][0] = {5: 5}
print(list(a[0][0].values())[0])

# # print(1 in b)
# # b=[1],[2]
# # print(a[b])
# # b=[1,2,3,4,56,7,9,0]
# # b.remove(2)
# # print(b)


# import weakref

# # Базовый класс для автоматического трекинга экземпляров
# class Trackable:
#     _registry = weakref.WeakSet()

#     def __new__(cls, *args, **kwargs):
#         instance = super().__new__(cls)
#         cls._registry.add(instance)
#         return instance

# # Родительские классы с трекингом
# class ParentA(Trackable):
#     def parent_method(self):
#         print(f"ParentA method called on {id(self)}")

# class ParentB(Trackable):
#     def parent_method(self):
#         print(f"ParentB method called on {id(self)}")

# # Дочерний класс, работающий с несколькими родителями
# class Child(ParentA, ParentB):
#     def trigger_all_parent_methods(self):
#         # Вызываем parent_method() для всех экземпляров ParentA
#         for instance in ParentA._registry:
#             if isinstance(instance, ParentA):
#                 instance.parent_method()
        
#         # Вызываем parent_method() для всех экземпляров ParentB
#         for instance in ParentB._registry:
#             if isinstance(instance, ParentB):
#                 instance.parent_method()


# pa1 = ParentA()
# pa2 = ParentA()
# pb = ParentB()
# child = Child()

# child.trigger_all_parent_methods()
# # Вывод:
# # ParentA method called on ... (pa1, pa2, child)
# # ParentB method called on ... (pb, child)
# print(map(int,input('Введите x и y: ').split()))