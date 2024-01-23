"""#python program to find square root
num=int(input("Enter the number:"))
sqr=num**(1/2)
print("The square root of given number is:",sqr)

#program to calculate area of triangle
base=int(input("Enter base of the traingle:"))
height=int(input("Enter height of the triangle:"))
area=(1/2)*base*height
print("Are of triangle is:",area)

#program to swap two variables
var1=input("Enter a variable:")
var2=input("Enter second variable:")
temp=var2
var2=var1
var1=temp
print(var1,var2)

#program to check number is positive,negative or zero
num=int(input("Enter the number:"))
if num > 0 :
    print("Given number is positive")
elif num < 0:
    print("Given number is negative")
else:
    print("Given number is zero")
    
#program to check number is odd or even 
num=int(input("Enter the number:"))
if num % 2 == 0:
    print("Given number is even")
else:
    print("Given number is odd")

#program to check largest among three numbers
n1=int(input("Enter first number:"))
n2=int(input("Enter second number:"))
n3=int(input("Enter third number:"))
if n1>n2 and n1>n3:
    print("First number is greatest")
elif n2>n1 and n2>n3:
    print("Second number is greatest")
else:
    print("Third number is greatest")

#program to check given number is prime or not
num=int(input("Enter th number you want to check:"))
if num == 1:
    print(num, "is not a prime number")
elif num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
       
# if input number is less than
# or equal to 1, it is not prime
else:
   print(num,"is not a prime number")

#program to print multiplication table of given number
num=int(input("Enter the number:"))
print("The multiplication table of given number is:")
for i in range(1,11):
    print(num,"*" ,i,"=",(num*i))

    #by using while loop:
    while i <=10:
      print(num,"*" ,i,"=",(num*i))

#program to make a simple calculator
print("Welcome to your calculator!!!")
num1=int(input("Enter the number:"))
num2=int(input("Enter another number:"))
choice=input("What you want to do:")
if choice == "add":
    sum=num1+num2
    print("Sum of two numbers is",sum)
elif choice == "sub":
    diff=num1-num2
    print("difference of two numbers is",diff)
elif choice == "mul":
    mul=num1*num2
    print("product of two numbers is",mul)
elif choice=="div":
    div=num1/num2
    print("division of two numbers is",div)"""

#program to find even number from starting to ending number given by user
start=int(input("Enter your starting number: "))
end=int(input("Enter your ending number: "))
for i in range(start,end):
    if i % 2 == 0:
        print(i,end=" ")


    







    
