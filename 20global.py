# l=10 #global

# def function1(n):
#     global l
#     l=l+45
#     m=6
#     print(l,m)
#     # l=5
#     print(n,"I have printed")
#     print(l,m)

# function1("this is me ")
# print(l)
# # print(m)

x=23

def harry():
    x=20
    def rohan():
        global x
        x=67


    print("before calling rohan() ", x)
    rohan()
    print("after calling rohan() ", x)
harry()
print(x)