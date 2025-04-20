# class ClassA(object):
#     def __init__(self, var1=5, var2=6):
#         ClassA.var1 = var1
#         ClassA.var2 = var2

#     def methodA(self):
#         ClassA.var1 = ClassA.var1 + ClassA.var2
#         return ClassA.var1



# class ClassB(ClassA):
#     def __init__(self):
#         print( ClassA.var1)
#         print (ClassA.var2)

# object1 = ClassA()
# sum = object1.methodA()
# object2 = ClassB()
a=[[i for i in range(1,10)]]*10
print(a)
b=[1,2]
print(a[b])