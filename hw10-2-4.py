#Author: ALJ (AMDG) 12/9/20

def letters(word1, letter1):
    total_letters = 0
    for x in word1:
        if x == letter1:
            total_letters += 1
    print("The total amount of {0}'s in {1} is {2}.".format(letter1, word1, total_letters))

letters('supercalifragilisticexpialidocious', 'i')