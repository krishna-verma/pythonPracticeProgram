def sum_function(*numbers):
    total = 0
    for i in numbers:
        total += i

    return total/len(numbers)
    
print(sum_function(1,2,3,4,5))
