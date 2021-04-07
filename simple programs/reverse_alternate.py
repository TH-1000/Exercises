# Reverse every other word in a string... This exercise is from https://www.codewars.com/kata/58d76854024c72c3e20000de
"""
Reverse every other word in a given string, then return the string. Throw away any leading or trailing whitespace,
while ensuring there is exactly one space between each word. Punctuation marks should be treated as if they are a part
of the word in this kata.
"""

def reverse_alternate(string):
    word_list = []
    reverse_list = []
    # choose the words
    for word in string.split():
        if string.split().index(word) % 2 == 0:   # even index words
            word_list.append(word)
            continue
        else:                                     # reverse the other words in another list
            for i in word:
                reverse_list.append(i)
                continue
            reverse_list.reverse()
            rev_word = ''.join(reverse_list)
            word_list.append(rev_word)
            reverse_list = []
    # join the list
    alternate = ' '.join(word_list)
    return alternate


print(reverse_alternate('I really hope it works this time around!...'))
# Output : I yllaer hope ti works siht time ...!dnuora
