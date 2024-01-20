start=int(input("Enter the starting interval to find prime numbers:"))
stop=int(input("Enter the starting interval to find prime numbers:"))
for num in range(start,stop):
    if num >1:
        for i in range(2,num):
            if num%i == 0:
                break
        else:
            print(num)
