# ------------------------------Variable and instance
'''
two types of variable:
-instance variable:jati ota variable banayeni naya memory ma rakhxa.access garna instance method chainxa which contain self parmater in it first arguments
-class variable/static:variable which have single copy of every object
-class method:access class variable with cls in first argument
# '''
# --------------instance variable
class Student:
    def __init__(self):
        self.name="sujan"
        print(self.name)      
a=Student()
a.name="Ram"  '''instance variable access outside the class'''
a.show()

b=Student()
b.show()

# ---------------------------class variable
class Student:
    school="Prime"
    def __init__(self):
        self.name="sujan"
    def show(cls):
        print(cls.school) 
a=Student()
Student.school="united"
a.show()

# ----------------------static variableor method: class ra instance variable nachaiyeko bela static variable use hunxa
class Student:
    school="Prime"
    def __init__(self):
        self.name="sujan"
    @staticmethod
    def show():
        print("print") 
a=Student()
Student.school="united"
a.show()

# -----------------------------nested class
class Student:
    def __init__(self):
        self.name="sujan"
        self.d=self.Std()

    def show(self):
        print(self.name)
    class Std:
        def __init__(self):
            self.age=24
        def show1(self):
            print(self.age)

a=Student()
b=a.Std()
b.show1()



