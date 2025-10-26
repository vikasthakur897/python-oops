string = 'hello'

x = 1
print(string.upper()) # Using method of string class
print(type(string))  # Checking type of variable

# Instance Method

class Student:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Name:", self.name)


# Class Method

class Student:
    college = "PTU"

    @classmethod
    def change_college(cls, new_name):
        cls.college = new_name


# Static Method

class Math:
    @staticmethod
    def add(a, b):
        return a + b

print(Math.add(5, 3))  # 8


