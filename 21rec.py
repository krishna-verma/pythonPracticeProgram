# def factorial_alternative(n):
#     fac=1
#     for i in range (n):
#         fac=fac*(i+1)
#     return fac

# number = int(input("enter the number "))
# print("factorial using alternative method ",factorial_alternative(number))



def factorial_recurssion(n):
    if (n==1):
        return (1)
    else:
        return n*factorial_recurssion(n-1)

number = int(input("enter the number "))
print("factorial using alternative method ",factorial_recurssion(number))
