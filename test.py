# find the second largest number from the list without using inbuilt function
list1 = []

for i in range(int(input("Enter the number of elements to add in list: "))):
    list1.append(int(input("Enter the element: "))) 

def Method3(list1):  
    SL_Val = list1[0] 
    L_Val = list1[0] 
    for i in range(len(list1)):  
        if list1[i] > L_Val:  
            L_Val = list1[i]  
  
    for i in range(len(list1)):  
        if list1[i] > SL_Val and list1[i] != L_Val:
            SL_Val = list1[i] 
  
    return SL_Val
    
x = Method3(list1)
print("The second largest element in the list is", x)



        




# wap to display all prime numbers within an interval
# start=int(input("Enter the starting interval:"))
# end=int(input("Enter the ending interval:"))
# for num in range(start,end):
#     if num > 1:
#         for i in range(2,num):
#             if num%i == 0:
#                 break
#         else:
#             print(num)
        


#find fibonacci series
# a=0
# b=1
# n=int(input("Enter the number you want fibonacci series upto: "))
# if n < 0:
#     print("Please provide positive integer:")
# elif n == 1:
#     print(a)
# else:
#     print(a)
#     print(b)
#     for i in range(1,n+1):
#         c=a+b
#         a=b
#         b=c
#         print(c)
            
# find multiplication number of n 
# num=int(input("Enter the number:"))
# print(f"The multiplication table of {num} is:")
# for i in range(1,11):
#     print(num,"*" ,i,"=",(num*i))

# Write a function that takes a list of integer as input and returns a new list with elements sorted in descending order,
# but with all odd numbers appearing before all even numbers
# def fu():
#     list1 =[]
#     list3=[]
#     list4=[]
#     list5=[]
#     for i in range(5):
#         num=input("Enter the number of integers:\n")
#         list1.append(int(num))
#         print(list1)
    
#     for j in list1:
#                  if j % 2 != 0:
#                     list3.append(j)
#                  else:
#                     list4.append(j)

#     list3.sort(reverse=True)
#     list4.sort(reverse=True)
#     list5=list3+list4
#     print(list5)
# fu()





 


