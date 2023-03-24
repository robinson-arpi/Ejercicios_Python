#Training on Mexican Wave | Codewars
#https://www.codewars.com/kata/58f5c63f1e26ecda7e000029/train/python

def wave(s):
    words = []
    for i in range(len(s)):
        if s[i] == " ":
            continue
        words.append(s[:i] + s[i].upper() + s[i+1:])
    return words
