# ------------------Create a program that takes a user's name and age as input and prints a greeting message
name=input("Enter your name: ")
age=int(input("Enter your age: "))
message=print(f"Hello {name}, I hope this message finds you well!.I want to say you that you have been selected as a python developer for our company at age of {age} which is surprising for us. ")
print(message)

#--------------------Given a list of numbers, find the maximum and minimum values.
numbers=[11,12,89,14,7,56,63]
print(max(numbers))
print(min(numbers))

#------------------Create a Python function to check if a given string is a palindrome.
number="ramar"
def fun() :
   if number == number[::-1]:
      print("It\'s a palindrome")
   else:
     print("It\'s not a palindrome")
fun()

#-----------------Calculate the compound interest for a given principal amount, interest rate, and time period.
def prin():
    amount=int(input("Enter the principle: "))
    interest_rate=int(input("Enter the rate: "))
    time_period=int(input("Enter the time period: "))
    Compound_Interest=(amount*interest_rate*time_period)/100
    print(f"Compound interest of your amount is {Compound_Interest}")
prin()

#-------------- Given a list of integers, find the sum of all positive numbers
num = (1, 4, 5, 5, 4, -1, -6, -4)
addition = 0

for i in num:
    if i > 0:
        addition += i

print(addition)

#-----------------( Create a program that takes a sentence as input and counts the number of words in it.

sentence = input("Enter the sentence: ")
char_count = 0

for char in sentence:
    if char != ' ':
        char_count += 1

# print("Number of characters in the sentence (excluding spaces):", char_count)

#------------------------Create a function to reverse a given string'
def reve():
    string=input("Enter the string to be reverse:")
    reverse_string=string[::-1]
    print(reverse_string)
reve()

# ----------------------------using for loop reversing name 
name="Susmita Lohani"
rev_name=" "
for char in range(len(name)-1,-1,-1):
    rev_name +=name[char]
print(rev_name)

#----------------Write a Python program to check if a given string is a pangram (contains all letters of the alphabet)'
string=input("Enter the string you want to check: ")
print(string.isalpha())

#--------------- Create a function to count the number of vowels in a given string
string=input("Enter the string: ")
char_count=0
for char in string:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        char_count += 1
    else:
        count=0
print(char_count)

#-----------------Create a loop that prints the first 10 even numbers.
for i in range(2,20):
    if i % 2 == 0:
        print(i)


    
