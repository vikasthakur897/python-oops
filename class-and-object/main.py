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