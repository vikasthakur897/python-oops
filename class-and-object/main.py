#Object
x = 1
y = 10 # Global variable

print(x + y)

def fuction():
    y = 2
    print(x)
    print(y)
fuction()

print(type(x))
print(y) 


#Class

class MyClass:
    x = 5
    y = 10

    def my_function(self):
        print("Hello from MyClass")
        print(self.x)

obj = MyClass()
obj.my_function()
print(obj.x)
print(MyClass.y)   


#Creating a simple class and Object

class Car: 
    def __init__(self, brand, model): # constructor
        self.brand = brand  #Attribute
        self.model = model
    
    def start_engine(self):  #Method
        print(f"{self.brand} engine started!")

#Creating Objects

car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

#Accessing Attributes and Methods
print(car1.brand)  # Output: Toyota
print(car2.model)  # Output: Civic