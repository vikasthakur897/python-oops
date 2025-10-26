class Demo:
    def add(self, a=None, b=None, c=None):
        if a and b and c:
            print(a + b + c)
        elif a and b:
            print(a + b)
        else:
            print("Provide at least two arguments")

d = Demo()
d.add(2, 3)
d.add(2, 3, 4)
