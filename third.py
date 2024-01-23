# ------------------------fibonacci series
a=0
b=1
n=int(input("ENter the number you want fibonacci series upto: "))
if n <0:
    print("Please provide positive integer:")
elif n ==1:
    print(a)
else:
    print(a)
    print(b)
    for i in range(1,n+1):
        c=a+b
        a=b
        b=c
        print(c)

# Write a Python function that takes a list of strings as input and returns a new list containing only the strings that are palindromes
def check_palindrome():
    list1=["susmita","sunus","ama","binita","ramar","sutus","narayan"]
    list2=[]
    for i in list1:
      if i[::]==i[::-1]:
        list2.append(i)
    print(list2)
check_palindrome()

# Write a Python program that takes a list of tuples, where each tuple contains a string and an integer, and  returns a new list containing 
# the tuples sorted by the length of the string,  with ties broken by the value of the integer.
    
list1=[("app",3),("b",2),("orangee",20),("grapess",3)]
list2=[]
result = []
for i in list1:
    list2.append(list(i))

for i in range(len(list1)-1):
    if len(list2[i][0])==len(list2[i+1][0]):
        if list2[i][1] > list2[i+1][1]:
            temp=list2[i+1]
            list2[i+1]=list2[i]
            list2[i]=temp

    elif len(list2[i][0]) > len(list2[i+1][0]):
        temp=list2[i+1]
        list2[i+1]=list2[i]
        list2[i]=temp
for i in list2:
    result.append(tuple(i))
print(result)

# from a list of number ,move all zero from the list: input=[1,2,0,4,5,0]   output=[1,2,4,5]
list=[1,2,0,4,5,0]
for i in list:
    if i == 0:
        list.remove(0)
print(list)

# write a program to display all prime number within an interval
start=int(input("Enter the starting interval to find prime numbers:"))
stop=int(input("Enter the starting interval to find prime numbers:"))
for num in range(start,stop):
    if num >1:
        for i in range(2,num):
            if num%i == 0:
                break
        else:
            print(num)

# wap to reverse string using for loop
name="Susmita lohani"         
rev_name=" "
for char in range(len(name)-1,-1,-1):
    rev_name +=name[char]
print(rev_name)

# Write a Python program to create a class representing a shopping cart. Include methods for adding and removing items, 
# and calculating the total price

class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item, price, quantity=1):
        if item in self.items:
            self.items[item]['quantity'] += quantity
        else:
            self.items[item] = {'price': price, 'quantity': quantity}

    def remove_item(self, item, quantity=1):
        if item in self.items:
            if self.items[item]['quantity'] <= quantity:
                del self.items[item]
            else:
                self.items[item]['quantity'] -= quantity

    def calculate_total_price(self):
        total_price = sum(item['price'] * item['quantity'] for item in self.items.values())
        return total_price

    def display_cart(self):
        print("Shopping Cart:")
        for item, details in self.items.items():
            print(f"{item} - Quantity: {details['quantity']}, Price per unit: ${details['price']:.2f}")

# Example usage:
cart = ShoppingCart()

cart.add_item('Apple', 1.5, 3)
cart.add_item('Banana', 0.75, 2)
cart.add_item('Orange', 1.0, 4)

cart.display_cart()

total_price = cart.calculate_total_price()
print(f"Total Price: ${total_price:.2f}")

cart.remove_item('Banana', 1)

cart.display_cart()

total_price_after_removal = cart.calculate_total_price()
print(f"Total Price after removal: ${total_price_after_removal:.2f}")
