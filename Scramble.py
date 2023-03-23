'''
https://www.codewars.com/kata/55c04b4cc56a697bb0000048/train/python

scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False
'''


def scramble(s1, s2):
    # create a dictionary to count the occurrences of each character in str1
    char_count = {}
    for char in s1:
        char_count[char] = char_count.get(char, 0) + 1
    
    # check if all characters in str2 can be found in char_count
    for char in s2:
        if char not in char_count or char_count[char] == 0:
            return False
        char_count[char] -= 1
    
    # if we get here, all characters in str2 were found in str1
    return True

scramble('rkqodlw', 'world')
