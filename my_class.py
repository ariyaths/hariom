import time
# import pandas

print("my class")


class Character:
    def __init__(self, name):
        self.name2 = name

    def running(self):
        print("{} is running".format(self.name2))


John = Character(name = "John")
John.running()
Mary = Character("Mary")
Mary.running()


class Person:
    def __init__(self, name, score):
        self.name4 = name
        self.score2 = score

    def info(self):
        print("I am {} and I have {}".format(self.name4, self.score2)); time.sleep(0.1)


class Mary2(Person):
    def __init__(self, name, score):
        self.name4 = name
        self.score2 = score


mary2 = Mary2("Mary", 4555)
mary2.info()


class John2(Person):
    def __init__(self, name, score):
        self.name4 = name
        self.score2 = score


john2 = John2("John", 4555)
john2.info()


class Parent:
    ## video 24
    ## not overriding method
    def myMethod(self):
        print("Calling parent method"); time.sleep(0.1)


class Child(Parent):
    def myMethod(self):
        print("Calling child class"); time.sleep(0.1)


class Parent2:
    ## overriding method
    def myMethod(self):
        print("Calling parent method"); time.sleep(0.1)


class Child2(Parent2):
    def myMethod(self):
        pass


class Vector:
    # video 25
    # very important
    # overloading operators and data handling
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return "Vector (%d, %d)" %(self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2);time.sleep(0.1)


class JustCounter:
    __secretCount = 0

    def count(self):
        self.__secretCount += 1
        print("self.__secretCount = ", self.__secretCount); time.sleep(0.1)


counter = JustCounter()
counter.count()
counter.count()
print("counter._JustCounter__secretCount = ", counter._JustCounter__secretCount); time.sleep(0.1)
