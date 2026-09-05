from abc import ABCMeta, abstractmethod

class Animal(metaclass = ABCMeta): # 声明抽象基类，不能直接被实例化。
    @abstractmethod # 声明抽象函数，子类必须重写，否则子类也抽象化
    def Speak(self):
        pass

class Cat(Animal):
    def Speak(self):
        print("喵！")
class Dog(Animal):
    def Speak(self):
        print("汪！")

cat = Cat()
dog = Dog()

cat.Speak()
dog.Speak()