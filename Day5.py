# ----------------------------Exception Handling:handling error occuring in the program so that execution of program doesn't stop
# syntax:
# try:
#     block of code 
# except:
#     code for error occur
# types of error:syntax error,logical error,runtime error
# except handle run time error


try:
    a=int(input("Enter the number: "))
    b=int(input("Enter the number: "))
    def show(a,b):
        name="sus"
        print(name[1])
        s=a+b
        print("Sum of a and b ",s)
    show(a,b)
except ValueError:
    print("you have value error")
except IndexError:
    print("you have index error")
finally:
    print("this is finally code")

# ------------------------
num=int(input("Enter your number"))
def show(num):
    try:
       s="susmita"
       print(s[9])
       return num
    except:
        print("this is for error")
        return 0
    finally:
        print("This is important code")
show(num)
print("Our importamt code")

