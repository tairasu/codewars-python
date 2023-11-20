# Simple, given a string of words, return the length of the shortest word(s).

# String will never be empty and you do not need to account for different data types.
    
# https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9/train/python

def find_short(s):
    shortest=s.split()[0]
    for word in s.split():
        if(len(word) < len(shortest)):
            shortest=word
    return len(shortest)