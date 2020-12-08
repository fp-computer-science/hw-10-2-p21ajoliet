#2. Write a function called `sum_odds` that takes a list uses a for loop 
#to find the sum of all of the odd numbers in the list. 
#The program should return `True` for each of the following tests:
#sum_odds([1, 2, 3, 4, 5, 6]) == 9
#sum_odds([1, 3, 5, 7, 9]) == 25
#sum_odds([2, 4, 6, 8, 10]) == 0

def count_odds(list1):
    odds = 0
    for i in list1:
        if i % 2 == 0:
            odds += 1
    print(odds)

count_odds([2, 4, 6, 8, 10])