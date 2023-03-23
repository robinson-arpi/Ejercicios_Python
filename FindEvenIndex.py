#Training on Equal Sides Of An Array | Codewars
def find_even_index(s):
    for i in range(len(s)):
        sum1 = sum(s[:i])
        sum2 = sum(s[i+1:])
        if sum1 == sum2:
            return i
    return -1