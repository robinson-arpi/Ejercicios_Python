
#Training on CamelCase Method | Codewars
#https://www.codewars.com/kata/587731fda577b3d1b0001196/train/python
def camel_case(s):
    words = s.split()
    for i in range(len(words)):
        words[i] = words[i][0].upper() + words[i][1:]
    return "".join(words)