#Author: ALJ (AMDG) 12/9/20

def sum_odds(list1):
    total_odds = 0
    for x in list1:
        if x % 2 != 0:
           total_odds += x
    return total_odds

print(sum_odds([2, 4, 6, 8, 10]))