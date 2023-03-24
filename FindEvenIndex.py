#Training on Equal Sides Of An Array | Codewars
#https://www.codewars.com/kata/5679aa472b8f57fb8c000047/train/python

def find_even_index(s):
    for i in range(len(s)):
        if sum(s[:i]) == sum(s[i+1:]):
            return i
    return -1