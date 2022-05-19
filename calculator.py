#welcome to Rahul's calculator

#function to add
def addition(a,b):
    return a+b

#function for subtraction
def subtraction(a,b):
    return a-b

#function for multiplication
def multiplication(a,b):
    return a*b

#function for division
def division(a,b):
    if(b==0):
        print("you can't take divisior 0 : ")
        exit()
    return a/b

#function for modulo
def modulo(a,b):
    if(b==0):
        print("you can't take divisior 0 : ")
        exit()
    return a%b


print("In which type do you want to take number ")
print("""1. Int  2. Float""")
type = (input("Enter your choice 1 or 2 : "))
if type=="1":
    num1 = int(input("Enter the first number : "))
    num2 = int(input("Enter the second number : "))
if type=="2":
    num1 = float(input("Enter the first number : "))
    num2 = float(input("Enter the second number : "))

else:
    print("Invalid input please type 1 or 2 ")
    type = (input(""))
    if type=="1":
        num1 = int(input("Enter the first number : "))
        num2 = int(input("Enter the second number : "))
    if type=="2":
        num1 = float(input("Enter the first number : "))
        num2 = float(input("Enter the second number : "))

print("which operation d2o you want to perform : ")
print("""chose operator :
            1. Addition
            2. Subtraction
            3. Division
            4. Multiplication
            5. Modulo""")
print("""Enter     + for Addition
        - for Subtraction
        / for division
        * for multiplication
        % for modulo""")
optr = (input())
if optr == "+":
           result = addition(num1,num2)
           print("Result : a+b = ",result)

if optr == "-":
           result = subtraction(num1,num2)
           print("Result : a-b = ",result)

if optr == "/":
           result = division(num1,num2)
           print("Result : a/b = ",result)

if optr == "*":
           result = multiplication(num1,num2)
           print("Result : a*b = ",result)

if optr == "%":
           result = modulo(num1,num2)
           print("Result : a%b = ",result)


















