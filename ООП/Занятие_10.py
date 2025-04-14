class Animal:
    def speak(self):
        return "Издает звук"

class MixinSwim:
    def swim(self):
        return "Плавает"

class MixinFly:
    def fly(self):
        return "Летает"

class Duck(Animal, MixinSwim, MixinFly):
    def speak(self):
        return "Кря-кря"

class Penguin(Animal, MixinSwim):
    def speak(self):
        return "Буль-буль"



duck=Duck()
penguin=Penguin()



print(f"Говорит: {duck.speak()}")
print(f"Плавание: {duck.swim()}")  
print(f"Полёт: {duck.fly()}")
    
print(f"Говорит: {penguin.speak()}")
print(f"Плавание: {penguin.swim()}")  

