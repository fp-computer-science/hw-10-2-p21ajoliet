#Author: ALJ (AMDG) 12/9/20

def three_letter_words(list1):
    total_words = 0
    for x in list1:
        if len(x) == 3:
            total_words += 1
    return total_words

print(three_letter_words(['hop', 'pop', 'bop']))