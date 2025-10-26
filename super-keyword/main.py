class Parent:
    def __init__(self):
        print("Parent Constructor")

class Child(Parent):
    def __init__(self):
        super().__init__()  # call parent constructor
        print("Child Constructor")

c = Child()
