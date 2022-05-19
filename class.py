class student:
    pass

harry = student()
larry = student()

print(harry,larry)

harry.name = "Harry"
harry.std = 12
harry.section = 1

larry.name = "larry"
larry.std = 145
larry.section = 2
larry.subjects = ["hindi","english"]

print(harry.section,larry.std,larry.subjects)
