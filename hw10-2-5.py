#Author: ALJ (AMDG) 12/10/20

def sum_elements(list1):
    total = 0
    for x in list1:
        if x % 2 == 0:
            total += x
    return total

print(sum_elements([2, 4, 6, 8, 9]))