# Special methods that begin and end with double underscores.

#  Method        Description                
# -----------  -------------------------- 
# `__init__`     Constructor                
# `__str__`      String representation      
# `__len__`      Length of object           
# `__add__`      Operator overloading for +
# `__eq__`       == comparison              



class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return self.pages + other.pages

b1 = Book(100)
b2 = Book(150)
print(b1 + b2)  # 250
