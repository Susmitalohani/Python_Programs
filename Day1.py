# Oops concept:variable haru lai real world entity match garxa
# class and objects
# class:blueprint of object or collection of object or template of creting objects
# object:instance of class
# class:group of attribute and method
# attribute:represent variable which hold data or characteristics
# methods:similar to function or perform a action or task
# Namespace:



''' syntax:
           class Classname(object): -----------class
             def_init_(self): ----------method
               self.variable_name="susmita" -------------attributes
               self.variable_Age=24

             def show(self):
                body of code
            a=ClassName() ----------object
            a.show()

            ------------------assert:validation
            assert condition error message
 '''

# ----------------------
# example:
class Student():
   def _init_(self,name):
    self.name=name
   def show(self,age):
      print(f"Hello World!!! my name is {self.name} and age is {age}")
a=Student("Susmita")
a.show(24)

# -------------------
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(f"My name is {self.name}, my age is {self.age}")
a=Student("ram",27)
a.show()
b=Student("Susmita",24)
b.show()


# -----------------------Real_world_example
class Shop():
    def __init__(self,name,price,qty):
        # validation
        # assert qty>=0, f"Quantity {qty} should be greater than 0"
        # assert price>=0, f"Price {price} should be greater than 0"
        self.name=name
        self.price=price
        self.qty=qty
    def Totalprice(self):
        return self.price*self.qty
obj1=Shop("Book",200,-2)
print(obj1.Totalprice())
obj2=Shop("Pen",10,12)
print(obj2.Totalprice())





