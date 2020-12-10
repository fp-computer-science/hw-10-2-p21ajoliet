#5. Write a function that takes a list and sums up all the elements 
#in the list up to but not including the first odd number.
#Make sure the function can handle if there are no odd numbers in the list.
#The program should return `True` for each of the following tests
#Be sure to replace `your_function_name` with a name valid function name that better describes the function:
#    your_function_name([2, 4, 6, 8, 9]) == 20
#    your_function_name([13, 12, 10]) == 0
#    your_function_name([14, 16, 32]) == 62

def sum_elements(list1):
    total = 0
    for x in list1:
        total += x
    return total

print(sum_elements([2, 4, 6]))
