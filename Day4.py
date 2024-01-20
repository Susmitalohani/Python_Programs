# ----------------------Encapsulation:wrapping method and variable in a unit class
# class Student:
#     def __init_(self) -> None:
#         self.name="SUsmita"
#     def show(self):
#         print(self.name)

# a=Student()
# a.name="Ram"

# class A:
#     def __init__(self) ->None:
#         print(a.name)
# b=A()

# # It use private and protect to restrict from globally
# # _name:Protected 
# #  __name:Private 

# -----------------------Exampe:
# age protected thyo so access garna milxa 
# name private banako thyo so access garna milena 
# class Student:
#     __name="Susmita"
#     _age=23

#     def show(self):
#         print(self.__name)
#         print(self._age)
# a=Student()
# a.show()
# # print("My name is",a.__name)
# print("My age is",a._age)

# -----------------------Abstraction:hiding complexity from user
# yesma len le kasari kam gariraxa sabai hide gareko matra action perform garirako xa this is abstraction
# a="Susmita"
# print(len(a))
# yo sum1 bhanne next file ho jasle sumation bahnne function banako xa tesailai call garya yeta 

# import sum1
# sum1.sumation()

# ----------------------------Module:collection of variable ,function,class store in aa file
# borrow someone else code or own
# code reuseability
# two types of module: 2.user defined module
# 1.predefined module

# import calendar
# print(calendar.month(2024,1))

# import datetime
# a=datetime.datetime.now()
# print(a)

# print(max(3,9,15))

# import math
# print(math.sqrt(36))

# from math import sqrt,ceil
# print(sqrt(36))
# print(ceil( 2.6))

# from math import *
# print(pow(5,2))
# print(floor(2.3))

# alias:name same xa bhane or name difficult xa bhane we use alias
# import math as m
# print(m.sqrt(36))

