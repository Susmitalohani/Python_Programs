# -------------------------------inheritance in python
# inheritance: child class(Derived  class) inherits properties and behaviour from parent class(base class)
# example:

class A:
    def show1(self):
        print("THis is parent class")
class B(A):
    def show2(Self):
        print("This is child class")

class C(B):
    def show3(self):
        print("This is derived class from B")
# a=A()
# a.show1()

# b=B()
# b.show2()
# b.show1()
c=C()
c.show1()
c.show2()
c.show3()

# ------------------------------------Multiple inheritance:

class A:
    def show1(self):
        print("THis is parentA")
class B:
    def show2(self):
        print("THis is parent B")
class C(A,B):
    def show3(self):
        print("THis is child")
c=C()
c.show1()
c.show2()
c.show3()

# ---------------------------------Polymorphism:hyaving multiple forms with same name 
# duck type

class Me:
    def show(self):
        print("THis is me")
class You:
    def show(self):
        print("This is you")
def display(var):
    var.show()
a=Me()
b=You()
display(a)
display(b)

# method overloading:class contain more than one method that can be sama name but different parameter

class Student:
    def __init__(self,name='',age=''):
        self.name=name
        self.age=age
        
    def show(self):
        print(self.name)
        print(self.age)
a=Student("Susmita")
a.show()

# ------------------------------eg:2

class Student:
    def sum(Self,a=None,b=None):
        s=0
        if a !=None and b== None:
            s=a
        elif b!= None and a == None:
            s=b
        elif a == None and b == None:
            s==a==b
        else:
            s=a+b
        return s
var=Student()
print(var.sum())

# method overriding

class A:
    def show(self):
        print("THis is me")
class B(A):
    def show(Self):
        # super().show()
        print("This is you")
a=B()
a.show()


# --------------------------abstraction:chaiyeko matraii dekhaune natra aru hide garera rakhne

a="Susmita"
print(len(a))
