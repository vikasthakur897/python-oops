class Student:
    college = "PTU"   # Class variable

    def __init__(self, name):
        self.name = name  # Instance variable

s1 = Student("Vikas")
s2 = Student("Aman")

print(s1.college)  # PTU
print(s2.college)  # PTU

Student.college = "IIT"  # Changing class variable
print(s1.college)        # IIT
