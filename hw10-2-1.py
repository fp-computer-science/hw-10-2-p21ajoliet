#Author: ALJ (AMDG) 12/7/20

def count_odds(list1):
    odds = 0
    for i in list1:
        if i % 2 == 0:
            odds += 1
    return odds

print(count_odds([2, 4, 6, 8, 10]))

#does this not count evens? line 6 would change to != to count odds