# --------------------------------------Homework:Function
'''Write a Python function that takes a list of integers as
 input and returns a new list with the elements sorted in descending order,
 but with all odd numbers appearing before all even numbers'''

def fu():
        list1=[4,5,6,7,8,9]
        list3=[]
        list4=[]
        list5=[]
        for i in list1:
                 if i % 2 != 0:
                    list3.append(i)
                 else:
                    list4.append(i)

        list3.sort(reverse=True)
        list4.sort(reverse=True)
        list5=list3+list4
        # list5.append(list3)
        # list5.append(list4)
        print(list5)
fu()

# -----------------------------------Homework:class and objects
# Write a program to convert Celsius to Fahrenheit  only using class and object
input1=36
class cel_to_fahre:
    def __init__(self,Celcius):
        self.Celcius=Celcius*(9/5)+32
temp1=cel_to_fahre(input1)
print(f"{input1} degree in fahrenheit is {temp1.Celcius}")

# --------------------------------------
# from a list of number ,move all zero from the list: input=[1,2,0,4,5,0]   output=[1,2,4,5]
list1=[1,2,0,4,5,0]
for  i in list1:
     if i == 0:
          list1.pop(0)
          print(list1)

# --------------------------------
# write a program to display all prime number within an interval
start=int(input("Enter the starting interval to find prime numbers:"))
stop=int(input("Enter the starting interval to find prime numbers:"))
for num in range(start,stop):
    if num >1:
        for i in range(2,num):
            if num%i == 0:
                break
        else:
            print(num)
     
