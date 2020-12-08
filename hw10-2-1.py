#Author: ALJ (AMDG) 12/7/20

def count_odds(list1):
    odds = 0
    for i in list1:
        if i % 2 == 0:
            odds += 1
    print(odds)

count_odds([2, 4, 6, 8, 10])