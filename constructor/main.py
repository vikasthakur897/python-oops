class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")    

student1 = Student("Alice", 20)
student2 = Student("Bob", 22)

student1.display()
student2.display()