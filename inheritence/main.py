# Single inheritance example

class Parent:
    def display(self):
        print("I am Parent")

class Child(Parent):
    def show(self):
        print("I am Child")

c = Child()
c.display()
c.show()


# Multilevel inheritance example

class Grandfather:
    def func1(self):
        print("Grandfather")

class Father(Grandfather):
    def func2(self):
        print("Father")

class Son(Father):
    def func3(self):
        print("Son")

s = Son()
s.func1()
s.func2()
s.func3()


#Multiple inheritance example

class Mother:
    def speak(self):
        print("Mother speaking")

class Father:
    def speak(self):
        print("Father speaking")

class Child(Mother, Father):
    def greet(self):
        print("Child says hello")

c = Child()
c.speak()

