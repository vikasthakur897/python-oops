# 🧠 Python OOP – All Definitions

## 1. Class 🏗️
A **class** is a blueprint for creating objects. It defines attributes (data) and methods (functions).

## 2. Object 📦
An **object** is an instance of a class that holds data and behavior defined by the class.

## 3. Constructor (`__init__`)  ⚙️
A **constructor** is a special method automatically called when an object is created. It initializes the object's attributes.

# 🧩 Types of Variables

##  4. Instance Variable
A variable defined inside a method and associated with a specific object (instance).

## 5. Class Variable
A variable shared by all objects of a class. Defined inside the class but outside methods.

# 🧱 Types of Methods

## 6. Instance Method
A method that operates on instance variables and requires `self` as the first parameter.

## 7. Class Method
A method that works with class variables and uses the `@classmethod` decorator. It takes `cls` as its first parameter.

## 8. Static Method
A method that does not depend on class or instance data. It uses the `@staticmethod` decorator.

## 9. Inheritance 🧬
A mechanism where one class (child) can derive properties and methods from another class (parent).

## 10. Method Overriding 🔁
Defining a method in the child class with the same name as in the parent class to provide a new implementation.

## 11. Method Overloading (Conceptual) 🔄
Having multiple methods with the same name but different parameters. In Python, it’s simulated using default arguments.

## 12. Encapsulation 💊
The concept of hiding data (attributes) using private or protected members to restrict direct access.

## 13. Abstraction 🔒
Hiding complex implementation details and showing only the necessary features using abstract classes or methods.

## 14. Polymorphism 🎭
The ability of different objects to respond differently to the same function or method call.

## 15. Super() 🧱
A built-in function used to call parent class methods or constructors from a child class.

## 16. Dunder (Magic) Methods 🧩
Special methods with double underscores (e.g., `__init__`, `__str__`, `__add__`) that define object behavior.

## 17. Composition 🏗️
A "has-a" relationship where one class contains another class as a part of its structure.

## 18. Operator Overloading 🧮
Redefining the behavior of operators (like `+`, `==`) for user-defined objects using dunder methods.

## 19. Destructor (`__del__`) 🚧
A special method automatically called when an object is deleted or goes out of scope, used for cleanup operations.

---

**🧱 Summary of Key OOP Principles:**  
- **Encapsulation** → Data Protection  
- **Abstraction** → Hiding Implementation  
- **Inheritance** → Code Reuse  
- **Polymorphism** → Many Forms (same interface, different behavior)
