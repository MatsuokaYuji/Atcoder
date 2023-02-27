





import string
upperAlpha = string.ascii_uppercase

d = set(upperAlpha)

S = input()

s = list(S)

for i in range(len(s)):
    if s[i] in d:
        print(i+1)
        exit()