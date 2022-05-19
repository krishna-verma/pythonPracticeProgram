list1 = ["rahul",23,12,"raj",9,87,5]

for item in list1:
    if str(item).isnumeric() and item>6:
        print(item)
    